# parser.py
from lexer import Token
from fia_ast import *
from errors import ParseError

class ParserFIA:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.ligne_courante = 0

    def analyser(self):
        instructions = []
        while not self.est_a_la_fin() and not self.regarder_token().type == 'EOF':
            instruction = self.analyser_instruction()
            if instruction:
                instructions.append(instruction)
        return Programme(instructions)

    def est_a_la_fin(self):
        return self.position >= len(self.tokens)

    def regarder_token(self):
        if self.est_a_la_fin():
            return Token('EOF', '', 0, 0)
        return self.tokens[self.position]

    def consommer_token(self, type_attendu=None):
        token = self.regarder_token()
        if type_attendu and token.type != type_attendu:
            raise ParseError(f"Erreur de syntaxe: attendu '{type_attendu}', trouvé '{token.type}' à la ligne {token.ligne}")
        self.position += 1
        return token

    def analyser_instruction(self):
        token = self.regarder_token()
        if token.type == 'SOIT':
            return self.analyser_declaration_variable()
        elif token.type == 'FONCTION':
            return self.analyser_fonction()
        elif token.type == 'RETOURNER':
            return self.analyser_retour()
        elif token.type == 'SI':
            return self.analyser_condition()
        elif token.type == 'TANT_QUE':
            return self.analyser_boucle_tant_que()
        elif token.type == 'POUR':
            return self.analyser_boucle_pour()
        elif token.type == 'IDENTIFIANT':
            # Vérifier si c'est une assignation (x = ...) ou un accès indexé (x[0] = ...)
            if self.position + 1 < len(self.tokens):
                if self.tokens[self.position + 1].type == 'ASSIGNATION':
                    return self.analyser_assignation()
                # Gérer le cas où c'est une expression avec accès indexé suivi d'assignation
                # Ex: liste[0] = 10
                # Le token courant est 'IDENTIFIANT', le suivant est 'CROCHET_OUVRANT'
                # On devra appeler analyser_expression_primaire pour traiter 'liste[0]'
                # et vérifier si le token après l'accès indexé est ASSIGNATION
                # Cela se fait dans analyser_assignation_expression
            # Sinon, c'est une expression (appel de fonction, variable seule, etc.)
            expr = self.analyser_expression()
            # Rendre le point-virgule optionnel ici aussi
            if self.regarder_token().type == 'POINT_VIRGULE':
                self.consommer_token('POINT_VIRGULE')
            return ExpressionStatement(expr)
        else:
            # Pour les expressions qui ne commencent pas par un identifiant
            expr = self.analyser_expression()
            # Rendre le point-virgule optionnel ici aussi
            if self.regarder_token().type == 'POINT_VIRGULE':
                self.consommer_token('POINT_VIRGULE')
            return ExpressionStatement(expr)

    def analyser_declaration_variable(self):
        self.consommer_token('SOIT')
        nom = self.consommer_token('IDENTIFIANT').valeur
        valeur = None
        if self.regarder_token().type == 'ASSIGNATION':
            self.consommer_token('ASSIGNATION')
            valeur = self.analyser_expression()
        # RENDRE LE POINT-VIRGULE OPTIONNEL
        if self.regarder_token().type == 'POINT_VIRGULE':
            self.consommer_token('POINT_VIRGULE')
        # --- FIN CHANGEMENT ---
        return DeclarationVariable(nom, valeur)

    def analyser_assignation(self):
        cible = self.analyser_primaire() # Pour gérer `liste[0] = ...`
        if self.regarder_token().type != 'ASSIGNATION':
            raise ParseError(f"Erreur de syntaxe: assignation attendue, trouvé '{self.regarder_token().type}'")
        self.consommer_token('ASSIGNATION')
        valeur = self.analyser_expression()
        # RENDRE LE POINT-VIRGULE OPTIONNEL
        if self.regarder_token().type == 'POINT_VIRGULE':
            self.consommer_token('POINT_VIRGULE')
        # --- FIN CHANGEMENT ---
        return Assignation(cible, valeur)

    def analyser_fonction(self):
        self.consommer_token('FONCTION')
        nom = self.consommer_token('IDENTIFIANT').valeur
        self.consommer_token('PARENTHESE_OUVRANTE')
        params = []
        if self.regarder_token().type != 'PARENTHESE_FERMANTE':
            params.append(self.consommer_token('IDENTIFIANT').valeur)
            while self.regarder_token().type == 'VIRGULE':
                self.consommer_token('VIRGULE')
                params.append(self.consommer_token('IDENTIFIANT').valeur)
        self.consommer_token('PARENTHESE_FERMANTE')
        corps = self.analyser_bloc()
        return Fonction(nom, params, corps)

    def analyser_retour(self):
        self.consommer_token('RETOURNER')
        valeur = None
        if self.regarder_token().type != 'POINT_VIRGULE' and self.regarder_token().type != 'ACCOLADE_FERMANTE': # Si ce n'est pas immédiatement un ';'
            valeur = self.analyser_expression()
        # RENDRE LE POINT-VIRGULE OPTIONNEL
        if self.regarder_token().type == 'POINT_VIRGULE':
            self.consommer_token('POINT_VIRGULE')
        # --- FIN CHANGEMENT ---
        return Retour(valeur)

    def analyser_condition(self):
        self.consommer_token('SI')
        self.consommer_token('PARENTHESE_OUVRANTE')
        condition = self.analyser_expression()
        self.consommer_token('PARENTHESE_FERMANTE')
        bloc_si = self.analyser_bloc()
        bloc_sinon = None
        if self.regarder_token().type == 'SINON':
            self.consommer_token('SINON')
            bloc_sinon = self.analyser_bloc()
        return Condition(condition, bloc_si, bloc_sinon)

    def analyser_boucle_tant_que(self):
        self.consommer_token('TANT_QUE')
        self.consommer_token('PARENTHESE_OUVRANTE')
        condition = self.analyser_expression()
        self.consommer_token('PARENTHESE_FERMANTE')
        corps = self.analyser_bloc()
        return BoucleTantQue(condition, corps)

    def analyser_boucle_pour(self):
        self.consommer_token('POUR')
        self.consommer_token('PARENTHESE_OUVRANTE')
        init = self.analyser_instruction()
        self.consommer_token('POINT_VIRGULE')
        condition = self.analyser_expression()
        self.consommer_token('POINT_VIRGULE')
        increment = self.analyser_instruction()
        self.consommer_token('PARENTHESE_FERMANTE')
        corps = self.analyser_bloc()
        return BouclePour(init, condition, increment, corps)

    def analyser_bloc(self):
        self.consommer_token('ACCOLADE_OUVRANTE')
        instructions = []
        while self.regarder_token().type != 'ACCOLADE_FERMANTE' and not self.est_a_la_fin():
            instruction = self.analyser_instruction()
            if instruction:
                instructions.append(instruction)
        self.consommer_token('ACCOLADE_FERMANTE')
        return Bloc(instructions)

    def analyser_expression(self):
        # Précédence des opérateurs
        return self.analyser_ou()

    def analyser_ou(self):
        gauche = self.analyser_et()
        while self.regarder_token().type == 'OU':
            operateur = self.consommer_token().valeur
            droite = self.analyser_et()
            gauche = ExpressionBinaire(gauche, operateur, droite)
        return gauche

    def analyser_et(self):
        gauche = self.analyser_comparaison()
        while self.regarder_token().type == 'ET':
            operateur = self.consommer_token().valeur
            droite = self.analyser_comparaison()
            gauche = ExpressionBinaire(gauche, operateur, droite)
        return gauche

    def analyser_comparaison(self):
        gauche = self.analyser_terme()
        while self.regarder_token().type in ['EGAL', 'DIFF', 'INF', 'SUP', 'INF_EGAL', 'SUP_EGAL']:
            operateur = self.consommer_token().valeur
            droite = self.analyser_terme()
            gauche = ExpressionBinaire(gauche, operateur, droite)
        return gauche

    def analyser_terme(self):
        gauche = self.analyser_facteur()
        while self.regarder_token().type in ['PLUS', 'MOINS']:
            operateur = self.consommer_token().valeur
            droite = self.analyser_facteur()
            gauche = ExpressionBinaire(gauche, operateur, droite)
        return gauche

    def analyser_facteur(self):
        gauche = self.analyser_unaire()
        while self.regarder_token().type in ['FOIS', 'DIVISE', 'MODULO']:
            operateur = self.consommer_token().valeur
            droite = self.analyser_unaire()
            gauche = ExpressionBinaire(gauche, operateur, droite)
        return gauche

    def analyser_unaire(self):
        # Gestion des opérateurs unaires (ex: -5, -variable)
        if self.regarder_token().type == 'MOINS': # Ajout de la gestion de l'opérateur unaire MOINS
            operateur = self.consommer_token().valeur
            operand = self.analyser_unaire() # Récursion pour gérer --5 ou -(-x)
            return ExpressionUnaire(operateur, operand)
        # Pour l'instant, on passe directement à la primaire
        return self.analyser_appel()

    def analyser_appel(self):
        gauche = self.analyser_primaire()

        while self.regarder_token().type in ['PARENTHESE_OUVRANTE', 'CROCHET_OUVRANT']: # Accès indexé
            if self.regarder_token().type == 'PARENTHESE_OUVRANTE':
                gauche = self.analyser_appel_fonction(gauche)
            elif self.regarder_token().type == 'CROCHET_OUVRANT':
                gauche = self.analyser_acces_index(gauche)
            else:
                break
        return gauche

    def analyser_appel_fonction(self, nom_fonction_noeud):
        self.consommer_token('PARENTHESE_OUVRANTE')
        arguments = []
        if self.regarder_token().type != 'PARENTHESE_FERMANTE':
            arguments.append(self.analyser_expression())
            while self.regarder_token().type == 'VIRGULE':
                self.consommer_token('VIRGULE')
                arguments.append(self.analyser_expression())
        self.consommer_token('PARENTHESE_FERMANTE')
        # Si le nom_fonction_noeud est un Identifiant, on extrait le nom
        if isinstance(nom_fonction_noeud, Identifiant):
            nom_fonction = nom_fonction_noeud.nom
        else:
             # Sinon, c'est une expression complexe (ex: obj.fonction)
             nom_fonction = nom_fonction_noeud # Pourrait être traité différemment si nécessaire
        return AppelFonction(nom_fonction, arguments)

    def analyser_acces_index(self, base_noeud):
        self.consommer_token('CROCHET_OUVRANT')
        index_expr = self.analyser_expression()
        self.consommer_token('CROCHET_FERMANT')
        return AccesIndex(base_noeud, index_expr)

    def analyser_primaire(self):
        token = self.regarder_token()
        if token.type == 'NOMBRE':
            self.consommer_token()
            return Littéral(token.valeur)
        elif token.type == 'CHAINE':
            self.consommer_token()
            return Littéral(token.valeur)
        elif token.type == 'VRAI':
            self.consommer_token()
            return Littéral(True)
        elif token.type == 'FAUX':
            self.consommer_token()
            return Littéral(False)
        elif token.type == 'NUL':
            self.consommer_token()
            return Littéral(None)
        elif token.type == 'CROCHET_OUVRANT':
            return self.analyser_liste()
        elif token.type == 'IDENTIFIANT' or token.type in ['IMPRIMER', 'LONGUEUR']:
            nom = self.consommer_token().valeur # Consommer le token, qu'il soit IDENTIFIANT, IMPRIMER ou LONGUEUR
            return Identifiant(nom)
        elif token.type == 'PARENTHESE_OUVRANTE':
            self.consommer_token('PARENTHESE_OUVRANTE')
            expr = self.analyser_expression()
            self.consommer_token('PARENTHESE_FERMANTE')
            return expr
        else:
            raise ParseError(f"Erreur de syntaxe: expression inattendue '{token.type}' à la ligne {token.ligne}")

    def analyser_liste(self):
        self.consommer_token() # '['
        elements = []
        if self.regarder_token().type != 'CROCHET_FERMANT':
            elements.append(self.analyser_expression())
            while self.regarder_token().type == 'VIRGULE':
                self.consommer_token('VIRGULE')
                elements.append(self.analyser_expression())
        self.consommer_token('CROCHET_FERMANT') # ']'
        return Littéral(elements)

# Exemple d'utilisation
if __name__ == "__main__":
    from lexer import LexerFIA
    code = """
    soit x = 10;
    si (x > 5) {
        imprimer("x est grand");
    }
    """
    lexer = LexerFIA(code)
    tokens = lexer.tokeniser()
    parser = ParserFIA(tokens)
    ast = parser.analyser()
    print(ast.instructions)
