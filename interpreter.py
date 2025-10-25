# interpreter.py
from errors import RuntimeError, ReturnException
import builtin
import ia_module  # Module IA maintenant activé
from fia_ast import Identifiant, AccesIndex, AccesDictionnaire, ExpressionStatement, Noeud

class VisiteurInterpretation:
    def __init__(self):
        # Utilisation d'une pile de contextes pour la portée des variables
        self.contextes = [{}]  # Pile de dictionnaires. Le premier est le contexte global.
        self.fonctions_integrees = builtin.FONCTIONS_INTEGREES.copy() # Copie des fonctions intégrées
        
        # ACTIVATION DU MODULE IA
        self.fonctions_integrees.update(ia_module.FONCTIONS_IA)  # Ajout des fonctions IA
        
        # Pour stocker les fonctions définies par l'utilisateur
        self.fonctions_definies = {}
        
        print("🤖 Module IA activé - Fonctions disponibles:")
        for nom_fonction in ia_module.FONCTIONS_IA.keys():
            print(f"   • {nom_fonction}()")

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
        elif isinstance(cible, AccesDictionnaire):
            # Assignation à une clé de dictionnaire
            base_dict = self.executer(cible.base)
            cle_value = self.executer(cible.cle)
            if not isinstance(base_dict, dict):
                raise RuntimeError("Erreur d'exécution: L'opérande gauche de l'assignation par clé doit être un dictionnaire")
            base_dict[cle_value] = valeur
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
        if self.contextes:
            self.contextes[-1][nom] = valeur
        else:
            # Fallback au contexte global
            self.contextes = [{}]
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

        # Exécuter et convertir les arguments
        args = [self.executer(arg) for arg in appel.arguments]
        # Convertir les objets AST en types Python natifs
        args_convertis = [self._convertir_en_python(arg) for arg in args]

        if nom_fonction in self.fonctions_integrees:
            fonction = self.fonctions_integrees[nom_fonction]
            try:
                return fonction(*args_convertis)  # Utiliser args_convertis
            except TypeError as e:
                raise RuntimeError(f"Erreur d'exécution lors de l'appel de '{nom_fonction}': {e}")
            except Exception as e:
                # Gestion des erreurs spécifiques du module IA
                raise RuntimeError(f"Erreur IA dans '{nom_fonction}': {str(e)}")
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

    def visiter_acces_dictionnaire(self, acces_dict):
        base_value = self.executer(acces_dict.base)
        cle_value = self.executer(acces_dict.cle)
        
        if not isinstance(base_value, dict):
            raise RuntimeError("Erreur d'exécution: L'opérande gauche de l'accès par clé doit être un dictionnaire")
        
        if cle_value not in base_value:
            raise RuntimeError(f"Erreur d'exécution: Clé '{cle_value}' non trouvée dans le dictionnaire")
        
        return base_value[cle_value]

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
        # Créer un nouveau contexte pour ce bloc
        self.contextes.append({})  # Nouveau contexte local
        
        resultat = None
        try:
            for instruction in bloc.instructions:
                resultat = self.executer(instruction)
        finally:
            # Fusionner les variables du bloc avec le contexte parent avant de le supprimer
            contexte_bloc = self.contextes.pop()  # Retirer le contexte du bloc
            if self.contextes:  # S'assurer qu'il reste un contexte parent
                self.contextes[-1].update(contexte_bloc)  # Fusionner avec le parent
        
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

    def _convertir_en_python(self, valeur):
        """Convertit récursivement les objets F-IA en types Python natifs."""
        # Import local pour éviter les imports circulaires
        from fia_ast import Littéral
        
        if isinstance(valeur, Littéral):
            # Si c'est un Littéral, convertir sa valeur
            return self._convertir_en_python(valeur.valeur)
        elif isinstance(valeur, list):
            # Convertir récursivement chaque élément de la liste
            return [self._convertir_en_python(item) for item in valeur]
        elif isinstance(valeur, dict):
            # Convertir récursivement chaque valeur du dictionnaire
            return {k: self._convertir_en_python(v) for k, v in valeur.items()}
        else:
            # Types Python de base : int, float, str, bool, None
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
    
    # Test IA
    soit modele = reseau_neuronal([2, 5, 1], "relu")
    soit donnees = charger_jeu_de_donnees("iris")
    """
    lexer = LexerFIA(code)
    tokens = lexer.tokeniser()
    parser = ParserFIA(tokens)
    ast = parser.analyser()
    interpreter = VisiteurInterpretation()
    interpreter.executer(ast)
    print("Variables globales:", interpreter.contextes[0])
