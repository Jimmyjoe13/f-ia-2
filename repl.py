# repl.py
from lexer import LexerFIA
from parser import ParserFIA
from interpreter import VisiteurInterpretation
from errors import FIAError
import sys

class REPL:
    def __init__(self):
        self.interpreter = VisiteurInterpretation()
        self.prompt = "f-ia> "

    def boucle(self):
        print("🌟" * 50)
        print("🤖 F-IA v0.2 - REPL Interactif")
        print("💻 Langage de programmation français pour l'IA")
        print("🎯 Amélioré avec ACCÈS INDEXÉ, OPÉRATEUR UNAIRE, ACCENTS!")
        print("🌟" * 50)
        print("Commandes spéciales: .aide, .variables, .reset, .quitter")
        print("🌟" * 50)
        while True:
            try:
                ligne = input(self.prompt).strip()
                if not ligne:
                    continue
                if ligne.startswith('.'):
                    self.executer_commande_speciale(ligne)
                else:
                    self.executer_ligne(ligne)
            except KeyboardInterrupt:
                print("\n🛑 Utilisez 'quitter' pour sortir")
            except EOFError:
                print("\n👋 Au revoir !")
                break

    def executer_commande_speciale(self, commande):
        if commande == '.aide':
            print("\n📚 AIDE F-IA:")
            print("  soit liste = [1, 2, 3]")
            print("  longueur(liste)")
            print("  soit x = 10")
            print("  x = x + 1")
            print("  si (x > 5) { imprimer(\"Grand\") }")
            print("  tant_que (i < 3) { imprimer(i); i = i + 1 }")
            print("  fonction doubler(n) { retourner n * 2; }") # Exemple avec 'retourner'
            print("  soit liste = [10, 20, 30]; imprimer(liste[0])") # Exemple avec accès indexé
            print("  soit neg = -5; imprimer(neg)") # Exemple avec opérateur unaire
            print("  soit nom_àccéntué = 'valeur'") # Exemple avec accents
        elif commande == '.variables':
            if not self.interpreter.contextes[0]: # Vérifie le contexte global
                print("📝 Aucune variable globale")
            else:
                print("\n📝 Variables globales:")
                for nom, valeur in self.interpreter.contextes[0].items(): # Accès au contexte global
                    print(f"  {nom} = {valeur}")
            if not self.interpreter.fonctions_definies:
                print("📝 Aucune fonction définie")
            else:
                print("\n📝 Fonctions définies:")
                for nom, _ in self.interpreter.fonctions_definies.items():
                    print(f"  {nom}")
        elif commande == '.reset':
            # Réinitialiser les contextes : un contexte global vide
            self.interpreter.contextes = [{}]
            # Réinitialiser les fonctions définies par l'utilisateur
            self.interpreter.fonctions_definies = {}
            print("🔄 Variables et fonctions réinitialisées")
        elif commande in ['.quitter', 'quitter']:
            print("👋 Au revoir !")
            sys.exit(0)
        else:
            print(f"Commande spéciale inconnue: {commande}")

    def executer_ligne(self, ligne):
        try:
            lexer = LexerFIA(ligne)
            tokens = lexer.tokeniser()
            print(f"🔤 Tokens: {tokens}")
            parser = ParserFIA(tokens)
            ast = parser.analyser()
            print(f"🌳 AST: {ast.instructions}")
            resultat = self.interpreter.executer(ast)
            if resultat is not None:
                print(f"🎯 Résultat: {resultat}")
        except FIAError as e:
            print(e)
        except Exception as e:
            print(f"Erreur inattendue: {e}")

if __name__ == "__main__":
    repl = REPL()
    repl.boucle()