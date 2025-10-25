# errors.py

class FIAError(Exception):
    """Classe de base pour les erreurs du langage F-IA."""
    pass

class LexerError(FIAError):
    """Erreur pendant l'analyse lexicale."""
    pass

class ParseError(FIAError):
    """Erreur pendant l'analyse syntaxique."""
    pass

class RuntimeError(FIAError):
    """Erreur pendant l'exécution du programme."""
    pass

# Exception spécifique pour gérer le 'retourner'
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value