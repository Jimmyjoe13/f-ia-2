# main.py
import sys
import os
from lexer import LexerFIA
from parser import ParserFIA
from interpreter import VisiteurInterpretation
from repl import REPL
from errors import FIAError

def executer_fichier(nom_fichier):
    if not os.path.exists(nom_fichier):
        print(f"Erreur: Le fichier '{nom_fichier}' n'existe pas.")
        return

    with open(nom_fichier, 'r', encoding='utf-8') as f:
        code_source = f.read()

    try:
        lexer = LexerFIA(code_source)
        tokens = lexer.tokeniser()
        parser = ParserFIA(tokens)
        ast = parser.analyser()
        interpreter = VisiteurInterpretation()
        interpreter.executer(ast)
    except FIAError as e:
        print(e)
    except Exception as e:
        print(f"Erreur inattendue lors de l'exécution de '{nom_fichier}': {e}")

def main():
    if len(sys.argv) > 1:
        nom_fichier = sys.argv[1]
        executer_fichier(nom_fichier)
    else:
        # Lancer le REPL si aucun fichier n'est fourni
        repl = REPL()
        repl.boucle()

if __name__ == "__main__":
    main()