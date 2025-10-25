# errors.py

class FIAError(Exception):
    """Classe de base pour les erreurs du langage F-IA."""
    pass

class LexerError(FIAError):
    """Erreur pendant l'analyse lexicale."""
    pass

class ParseError(FIAError):
    """Erreur pendant l'analyse syntaxique."""
    def __init__(self, message, ligne=None, colonne=None):
        super().__init__(message)
        self.ligne = ligne
        self.colonne = colonne
        
    def __str__(self):
        if self.ligne is not None and self.colonne is not None:
            return f"Erreur de syntaxe ligne {self.ligne}, colonne {self.colonne}: {self.args[0]}"
        return self.args[0]

class RuntimeError(FIAError):
    """Erreur pendant l'exécution du programme."""
    pass

# Exception spécifique pour gérer le 'retourner'
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value
