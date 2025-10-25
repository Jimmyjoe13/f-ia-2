# lexer.py
import re
from errors import LexerError

class Token:
    def __init__(self, type_token, valeur, ligne=0, colonne=0):
        self.type = type_token
        self.valeur = valeur
        self.ligne = ligne
        self.colonne = colonne

    def __repr__(self):
        return f"Token({self.type}, {self.valeur}, L{self.ligne}, C{self.colonne})"

class LexerFIA:
    def __init__(self, code_source):
        self.code = code_source
        self.position = 0
        self.ligne = 1
        self.colonne = 1
        self.tokens = []

        # Mots-clés
        self.mots_cles = {
            'soit': 'SOIT',
            'si': 'SI',
            'sinon': 'SINON',
            'pour': 'POUR',
            'tant_que': 'TANT_QUE',
            'fonction': 'FONCTION',
            'retourner': 'RETOURNER',
            'vrai': 'VRAI',
            'faux': 'FAUX',
            'nul': 'NUL',
            'et': 'ET',
            'ou': 'OU',
            'non': 'NON',
            'imprimer': 'IMPRIMER',
            'longueur': 'LONGUEUR',
            'arrondir': 'ARRONDIR',
            'aleatoire': 'ALEATOIRE',
            'racine': 'RACINE',
            'puissance': 'PUISSANCE',
            'entier': 'ENTIER',
            'chaine': 'CHAINE',
            'essayer': 'ESSAYER',
            'attraper': 'ATTRAPER',
            'importer': 'IMPORTER',
            'de': 'DE',
            # Ajouter les mots-clés IA ici si implémentés
            # 'reseau_neuronal': 'RESEAU_NEURONAL',
            # 'apprentissage': 'APPRENTISSAGE',
            # ...
        }

        # Symboles et opérateurs
        self.symboles = {
            '=': 'ASSIGNATION',
            '==': 'EGAL',
            '!=': 'DIFF',
            '<': 'INF',
            '<=': 'INF_EGAL',
            '>': 'SUP',
            '>=': 'SUP_EGAL',
            '+': 'PLUS',
            '-': 'MOINS', # Utilisé pour binaire et unaire
            '*': 'FOIS',
            '/': 'DIVISE',
            '%': 'MODULO',
            '(': 'PARENTHESE_OUVRANTE',
            ')': 'PARENTHESE_FERMANTE',
            '{': 'ACCOLADE_OUVRANTE',
            '}': 'ACCOLADE_FERMANTE',
            '[': 'CROCHET_OUVRANT',
            ']': 'CROCHET_FERMANT',
            '.': 'POINT',
            ',': 'VIRGULE',
            ':': 'DEUX_POINTS',
            ';': 'POINT_VIRGULE',
        }

    def tokeniser(self):
        while self.position < len(self.code):
            char = self.code[self.position]

            if char.isspace():
                if char == '\n':
                    self.ligne += 1
                    self.colonne = 1
                else:
                    self.colonne += 1
                self.avancer()
            elif char.isalpha() or char == '_' or self.est_accentue(char):
                self.traiter_mot_cle_ou_identifiant()
            elif char.isdigit():
                self.traiter_nombre()
            elif char in ['"', "'"]:
                self.traiter_chaine()
            elif self.traiter_symbole():
                continue # Symbole traité
            else:
                raise LexerError(f"Caractère inconnu '{char}' à la ligne {self.ligne}, colonne {self.colonne}")

        # Ajouter un token de fin
        self.tokens.append(Token('EOF', '', self.ligne, self.colonne))
        return self.tokens

    def est_accentue(self, char):
        # Vérifie si le caractère est un caractère accentué courant
        return '\u00C0' <= char <= '\u017F'

    def avancer(self):
        if self.position < len(self.code):
            if self.code[self.position] == '\n':
                self.ligne += 1
                self.colonne = 1
            else:
                self.colonne += 1
            self.position += 1

    def regarder(self, distance=1):
        pos = self.position + distance - 1
        if pos < len(self.code):
            return self.code[pos]
        return ''

    def traiter_mot_cle_ou_identifiant(self):
        debut = self.position
        while self.position < len(self.code) and (self.code[self.position].isalnum() or self.code[self.position] == '_' or self.est_accentue(self.code[self.position])):
            self.avancer()
        lexeme = self.code[debut:self.position]
        type_token = self.mots_cles.get(lexeme, 'IDENTIFIANT')
        self.tokens.append(Token(type_token, lexeme, self.ligne, debut - self.position + len(lexeme) + 1))

    def traiter_nombre(self):
        debut = self.position
        while self.position < len(self.code) and (self.code[self.position].isdigit() or self.code[self.position] == '.'):
            self.avancer()
        lexeme = self.code[debut:self.position]
        if '.' in lexeme:
            valeur = float(lexeme)
        else:
            valeur = int(lexeme)
        self.tokens.append(Token('NOMBRE', valeur, self.ligne, debut - self.position + len(lexeme) + 1))

    def traiter_chaine(self):
        quote_type = self.code[self.position]
        debut = self.position
        self.avancer() # Passer le quote d'ouverture
        while self.position < len(self.code) and self.code[self.position] != quote_type:
            if self.code[self.position] == '\n': # Pas de saut de ligne dans une chaîne
                raise LexerError(f"Chaîne non terminée à la ligne {self.ligne}")
            self.avancer()
        if self.position >= len(self.code):
            raise LexerError(f"Chaîne non terminée à la fin du fichier")
        self.avancer() # Passer le quote de fermeture
        lexeme = self.code[debut:self.position]
        valeur = lexeme[1:-1] # Enlever les quotes
        self.tokens.append(Token('CHAINE', valeur, self.ligne, debut - self.position + len(lexeme) + 1))

    def traiter_symbole(self):
        # Vérifier les symboles de longueur 2 en premier (==, !=, <=, >=)
        deux_car = self.code[self.position:self.position+2]
        if deux_car in self.symboles:
            self.tokens.append(Token(self.symboles[deux_car], deux_car, self.ligne, self.colonne))
            self.avancer()
            self.avancer()
            return True

        # Vérifier les symboles de longueur 1
        un_car = self.code[self.position]
        if un_car in self.symboles:
            self.tokens.append(Token(self.symboles[un_car], un_car, self.ligne, self.colonne))
            self.avancer()
            return True
        return False

# Exemple d'utilisation
if __name__ == "__main__":
    code = """
    soit x = 10;
    si (x > 5) {
        imprimer("x est grand");
    }
    """
    lexer = LexerFIA(code)
    tokens = lexer.tokeniser()
    for token in tokens:
        print(token)
