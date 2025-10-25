# builtin.py
import math
import random
from errors import RuntimeError

def imprimer(*args):
    print(*args)

def longueur(objet):
    if not isinstance(objet, (str, list)):
        raise RuntimeError("Erreur d'exécution: 'longueur' attend une chaîne ou une liste")
    return len(objet)

def arrondir(nombre, decimales=0):
    if not isinstance(nombre, (int, float)):
        raise RuntimeError("Erreur d'exécution: 'arrondir' attend un nombre")
    return round(nombre, decimales)

def aleatoire():
    return random.random()

def racine(nombre):
    if not isinstance(nombre, (int, float)) or nombre < 0:
        raise RuntimeError("Erreur d'exécution: 'racine' attend un nombre positif")
    return math.sqrt(nombre)

def puissance(base, exposant):
    if not isinstance(base, (int, float)) or not isinstance(exposant, (int, float)):
        raise RuntimeError("Erreur d'exécution: 'puissance' attend des nombres")
    return base ** exposant

def entier(valeur):
    try:
        return int(valeur)
    except (ValueError, TypeError):
        raise RuntimeError(f"Erreur d'exécution: impossible de convertir '{valeur}' en entier")

def chaine(valeur):
    return str(valeur)

# Dictionnaire des fonctions intégrées
FONCTIONS_INTEGREES = {
    'imprimer': imprimer,
    'longueur': longueur,
    'arrondir': arrondir,
    'aleatoire': aleatoire,
    'racine': racine,
    'puissance': puissance,
    'entier': entier,
    'chaine': chaine,
}