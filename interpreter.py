# interpreter.py
from errors import RuntimeError, ReturnException
import builtin
import ia_module # Importer si les fonctions IA sont activées
from fia_ast import Identifiant, AccesIndex, ExpressionStatement, Noeud # Importation des nœuds AST nécessaires

class VisiteurInterpretation:
    def __init__(self):
        # Utilisation d'une pile de contextes pour la portée des variables
        self.contextes = [{}]  # Pile de dictionnaires. Le premier est le contexte global.
        self.fonctions_integrees = builtin.FONCTIONS_INTEGREES.copy() # Copie des fonctions intégrées
        # self.fonctions_integrees.update(ia_module.FONCTIONS_IA) # Décommenter quand IA sera implémentée
        # Pour stocker les fonctions définies par l'utilisateur
        self.fonctions_definies = {}

    def executer(self, noeud_ast):
        return noeud_ast.accepter(self)

    def visiter_programme(self, programme):
        resultat = None
        for instruction in programme.instructions:
            resultat = self.executer(instruction)
        return resultat

    def visiter_declaration_variable(self, decl):
        valeur = self.executer(decl.valeur) if decl.valeur else None
        self._set_variable(decl.nom, valeur)

    def visiter_assignation(self, assign):
        valeur = self.executer(assign.valeur)
        cible = assign.cible
        if isinstance(cible, Identifiant):
            # Assignation à une variable simple
            if not self._variable_existe(cible.nom):
                raise RuntimeError(f"Erreur d'exécution: variable '{cible.nom}' non déclarée avant assignation")
            self._set_variable(cible.nom, valeur)
        elif isinstance(cible, AccesIndex):
            # Assignation à un index de liste
            base_list = self.executer(cible.base)
            index_value = self.executer(cible.index)
            if not isinstance(base_list, list):
                raise RuntimeError("Erreur d'exécution: L'opérande gauche de l'assignation par index doit être une liste")
            if not isinstance(index_value, int):
                raise RuntimeError("Erreur d'exécution: L'index doit être un entier")
            if index_value < 0 or index_value >= len(base_list):
                raise RuntimeError("Erreur d'exécution: Index de liste hors limites")
            base_list[index_value] = valeur
        else:
            raise RuntimeError(f"Erreur d'exécution: Cible d'assignation invalide")

    def _get_variable(self, nom):
        """Recherche une variable dans la pile des contextes."""
        for contexte in reversed(self.contextes): # Recherche du plus local au plus global
            if nom in contexte:
                return contexte[nom]
        raise RuntimeError(f"Erreur d'exécution: Variable '{nom}' non définie")

    def _variable_existe(self, nom):
        """Vérifie si une variable existe dans la pile des contextes."""
        for contexte in reversed(self.contextes):
            if nom in contexte:
                return True
        return False

    def _set_variable(self, nom, valeur):
        """Définit une variable dans le contexte local actuel."""
        if self.contextes: # S'assure qu'il y a au moins un contexte
            self.contextes[-1][nom] = valeur # Affecte dans le contexte du haut de la pile
        else:
            # Cas improbable si la pile est toujours initialisée
            self.contextes[0][nom] = valeur

    def visiter_expression_binaire(self, expr_bin):
        gauche = self.executer(expr_bin.gauche)
        droite = self.executer(expr_bin.droite)

        # Conversion des types si nécessaire
        gauche = self.convertir_si_nombre(gauche)
        droite = self.convertir_si_nombre(droite)

        op = expr_bin.operateur
        if op == '+': return gauche + droite
        elif op == '-': return gauche - droite
        elif op == '*': return gauche * droite
        elif op == '/':
            if droite == 0:
                raise RuntimeError("Erreur d'exécution: Division par zéro")
            return gauche / droite
        elif op == '%': return gauche % droite
        elif op == '==': return gauche == droite
        elif op == '!=': return gauche != droite
        elif op == '<': return gauche < droite
        elif op == '<=': return gauche <= droite
        elif op == '>': return gauche > droite
        elif op == '>=': return gauche >= droite
        elif op == 'et': return gauche and droite
        elif op == 'ou': return gauche or droite
        else:
            raise RuntimeError(f"Erreur d'exécution: Opérateur binaire inconnu: {op}")

    def visiter_expression_unaire(self, expr_unaire):
        operand_value = self.executer(expr_unaire.operande)
        operand_value = self.convertir_si_nombre(operand_value) # Convertir avant l'opération
        if expr_unaire.operateur == '-':
            return -operand_value
        elif expr_unaire.operateur == '+':
            return operand_value
        else:
            raise RuntimeError(f"Erreur d'exécution: Opérateur unaire non supporté: {expr_unaire.operateur}")

    def visiter_litteral(self, litteral):
        return litteral.valeur

    def visiter_identifiant(self, ident):
        nom = ident.nom
        if nom in self.fonctions_integrees or nom in self.fonctions_definies:
            # Si c'est une fonction, on la renvoie
            if nom in self.fonctions_integrees:
                return self.fonctions_integrees[nom]
            elif nom in self.fonctions_definies:
                return self.fonctions_definies[nom]
        else:
            # Sinon, c'est une variable
            return self._get_variable(nom)

    def visiter_appel_fonction(self, appel):
        nom_fonction = appel.nom_fonction

        args = [self.executer(arg) for arg in appel.arguments]
        if nom_fonction in self.fonctions_integrees:
            fonction = self.fonctions_integrees[nom_fonction]
            try:
                return fonction(*args)
            except TypeError as e:
                raise RuntimeError(f"Erreur d'exécution lors de l'appel de '{nom_fonction}': {e}")
        elif nom_fonction in self.fonctions_definies:
            # Appel d'une fonction définie par l'utilisateur
            func_def = self.fonctions_definies[nom_fonction]
            params = func_def['params']
            corps = func_def['corps']
            if len(args) != len(params):
                raise RuntimeError(f"Erreur d'exécution: la fonction '{nom_fonction}' attend {len(params)} arguments, {len(args)} fournis.")
            # Créer un contexte local pour les paramètres
            contexte_local = {}
            for param, arg in zip(params, args):
                contexte_local[param] = arg
            # Sauvegarder le contexte global
            ancien_contexte = self.contextes
            # Remplacer la pile par un nouveau contexte local
            self.contextes = [contexte_local]
            resultat_fonction = None
            try:
                for stmt in corps:
                    self.executer(stmt)
            except ReturnException as e:
                # Récupérer la valeur de retour si 'retourner' est exécuté
                resultat_fonction = e.value
            # Restaurer le contexte global
            self.contextes = ancien_contexte
            return resultat_fonction
        else:
            raise RuntimeError(f"Erreur d'exécution: fonction '{nom_fonction}' non définie")

    def visiter_acces_index(self, acces_index):
        base_value = self.executer(acces_index.base)
        index_value = self.executer(acces_index.index)
        if not isinstance(base_value, list):
            raise RuntimeError("Erreur d'exécution: L'opérande gauche de l'accès par index doit être une liste")
        if not isinstance(index_value, int):
            raise RuntimeError("Erreur d'exécution: L'index doit être un entier")
        if index_value < 0 or index_value >= len(base_value):
            raise RuntimeError("Erreur d'exécution: Index de liste hors limites")
        
        # Assurez-vous que l'élément récupéré est évalué s'il s'agit d'un nœud AST
        element = base_value[index_value]
        if isinstance(element, Noeud): # Si c'est un nœud AST, exécutez-le
            return self.executer(element)
        return element

    # --- Autres méthodes d'acceptation à implémenter ---
    def visiter_condition(self, condition):
        valeur_condition = self.executer(condition.condition)
        if valeur_condition:
            self.executer(condition.bloc_si) # bloc_si est un objet Bloc, il faut l'exécuter
        elif condition.bloc_sinon:
            self.executer(condition.bloc_sinon) # bloc_sinon est un objet Bloc, il faut l'exécuter

    def visiter_boucle_tant_que(self, boucle):
        condition_value = self.executer(boucle.condition)
        compteur = 0
        while condition_value and compteur < 50:
            self.executer(boucle.corps) # corps est un objet Bloc, il faut l'exécuter
            condition_value = self.executer(boucle.condition)
            compteur += 1
        if compteur >= 50:
            print("🛑 Sécurité: boucle arrêtée après 50 itérations")

    def visiter_boucle_pour(self, boucle):
        self.executer(boucle.init)
        condition_value = self.executer(boucle.condition)
        compteur = 0
        while condition_value and compteur < 50:
            self.executer(boucle.corps) # corps est un objet Bloc, il faut l'exécuter
            self.executer(boucle.increment)
            condition_value = self.executer(boucle.condition)
            compteur += 1
        if compteur >= 50:
            print("🛑 Sécurité: boucle arrêtée après 50 itérations")

    def visiter_bloc(self, bloc):
        resultat = None
        for instruction in bloc.instructions:
            resultat = self.executer(instruction)
        return resultat

    def visiter_fonction(self, fonction):
        # Enregistrer la fonction dans l'environnement global
        self.fonctions_definies[fonction.nom] = {'params': fonction.parametres, 'corps': fonction.corps}

    def visiter_retour(self, retour):
        valeur = self.executer(retour.valeur) if retour.valeur is not None else None
        # Lever une exception pour sortir de la fonction
        raise ReturnException(valeur)

    def visiter_expression_statement(self, stmt):
        return self.executer(stmt.expression)

    def convertir_si_nombre(self, valeur):
        """Convertit une valeur en nombre si possible"""
        if isinstance(valeur, str):
            if valeur.replace('.', '').replace('-', '').isdigit():
                return float(valeur) if '.' in valeur else int(valeur)
        return valeur

# Exemple d'utilisation
if __name__ == "__main__":
    from lexer import LexerFIA
    from parser import ParserFIA
    code = """
    soit x = 10;
    soit y = 20;
    soit somme = x + y;
    imprimer("La somme est ", somme);
    """
    lexer = LexerFIA(code)
    tokens = lexer.tokeniser()
    parser = ParserFIA(tokens)
    ast = parser.analyser()
    interpreter = VisiteurInterpretation()
    interpreter.executer(ast)
    print("Variables globales:", interpreter.contextes[0])
