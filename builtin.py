# builtin.py
import math
import random
from errors import RuntimeError

def imprimer(*args):
    print(*args)

def longueur(objet):
    if not isinstance(objet, (str, list, dict)):
        raise RuntimeError("Erreur d'exécution: 'longueur' attend une chaîne, une liste ou un dictionnaire")
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

# === NOUVELLES FONCTIONS DICTIONNAIRES ===

def cles(dictionnaire):
    """Retourne la liste des clés d'un dictionnaire."""
    if not isinstance(dictionnaire, dict):
        raise RuntimeError("Erreur d'exécution: 'cles' attend un dictionnaire")
    return list(dictionnaire.keys())

def valeurs(dictionnaire):
    """Retourne la liste des valeurs d'un dictionnaire."""
    if not isinstance(dictionnaire, dict):
        raise RuntimeError("Erreur d'exécution: 'valeurs' attend un dictionnaire")
    return list(dictionnaire.values())

def contient_cle(dictionnaire, cle):
    """Vérifie si une clé existe dans le dictionnaire."""
    if not isinstance(dictionnaire, dict):
        raise RuntimeError("Erreur d'exécution: 'contient_cle' attend un dictionnaire")
    return cle in dictionnaire

def supprimer_cle(dictionnaire, cle):
    """Supprime une clé du dictionnaire."""
    if not isinstance(dictionnaire, dict):
        raise RuntimeError("Erreur d'exécution: 'supprimer_cle' attend un dictionnaire")
    if cle not in dictionnaire:
        raise RuntimeError(f"Erreur d'exécution: clé '{cle}' non trouvée dans le dictionnaire")
    del dictionnaire[cle]
    return dictionnaire

def fusionner(dict1, dict2):
    """Fusionne deux dictionnaires."""
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise RuntimeError("Erreur d'exécution: 'fusionner' attend deux dictionnaires")
    resultat = dict1.copy()
    resultat.update(dict2)
    return resultat

def vider(dictionnaire):
    """Vide un dictionnaire."""
    if not isinstance(dictionnaire, dict):
        raise RuntimeError("Erreur d'exécution: 'vider' attend un dictionnaire")
    dictionnaire.clear()
    return dictionnaire

# === NOUVELLES FONCTIONS LISTES (CORRIGÉES) ===

def ajouter(liste, element):
    """Ajoute un élément à la fin d'une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'ajouter' attend une liste")
    liste.append(element)
    return liste  # Important : retourner la liste modifiée

def retirer(liste, index):
    """Retire un élément d'une liste par son index."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'retirer' attend une liste")
    if not isinstance(index, int):
        raise RuntimeError("Erreur d'exécution: 'retirer' attend un index entier")
    if index < 0 or index >= len(liste):
        raise RuntimeError("Erreur d'exécution: index hors limites")
    return liste.pop(index)

def trier(liste):
    """Trie une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'trier' attend une liste")
    liste.sort()
    return liste  # Important : retourner la liste modifiée

def inverser(liste):
    """Inverse l'ordre des éléments d'une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'inverser' attend une liste")
    liste.reverse()
    return liste

def copier(liste):
    """Crée une copie d'une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'copier' attend une liste")
    return liste.copy()

def contient(liste, element):
    """Vérifie si un élément est dans une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'contient' attend une liste")
    return element in liste

def index_de(liste, element):
    """Retourne l'index d'un élément dans une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'index_de' attend une liste")
    try:
        return liste.index(element)
    except ValueError:
        raise RuntimeError(f"Erreur d'exécution: élément '{element}' non trouvé dans la liste")

def compter(liste, element):
    """Compte le nombre d'occurrences d'un élément dans une liste."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'compter' attend une liste")
    return liste.count(element)

# === NOUVELLES FONCTIONS CHAÎNES ===

def majuscule(texte):
    """Convertit une chaîne en majuscules."""
    if not isinstance(texte, str):
        raise RuntimeError("Erreur d'exécution: 'majuscule' attend une chaîne")
    return texte.upper()

def minuscule(texte):
    """Convertit une chaîne en minuscules."""
    if not isinstance(texte, str):
        raise RuntimeError("Erreur d'exécution: 'minuscule' attend une chaîne")
    return texte.lower()

def remplacer(texte, ancien, nouveau):
    """Remplace toutes les occurrences d'une sous-chaîne."""
    if not isinstance(texte, str):
        raise RuntimeError("Erreur d'exécution: 'remplacer' attend une chaîne")
    return texte.replace(ancien, nouveau)

def diviser(texte, separateur=" "):
    """Divise une chaîne en liste selon un séparateur."""
    if not isinstance(texte, str):
        raise RuntimeError("Erreur d'exécution: 'diviser' attend une chaîne")
    return texte.split(separateur)

def joindre(liste, separateur=""):
    """Joint les éléments d'une liste en une chaîne."""
    if not isinstance(liste, list):
        raise RuntimeError("Erreur d'exécution: 'joindre' attend une liste")
    try:
        return separateur.join(str(item) for item in liste)
    except Exception:
        raise RuntimeError("Erreur d'exécution: impossible de joindre les éléments")

# Dictionnaire des fonctions intégrées
FONCTIONS_INTEGREES = {
    # Fonctions de base
    'imprimer': imprimer,
    'longueur': longueur,
    'arrondir': arrondir,
    'aleatoire': aleatoire,
    'racine': racine,
    'puissance': puissance,
    'entier': entier,
    'chaine': chaine,
    
    # Fonctions dictionnaires
    'cles': cles,
    'valeurs': valeurs,
    'contient_cle': contient_cle,
    'supprimer_cle': supprimer_cle,
    'fusionner': fusionner,
    'vider': vider,
    
    # Fonctions listes
    'ajouter': ajouter,
    'retirer': retirer,
    'trier': trier,
    'inverser': inverser,
    'copier': copier,
    'contient': contient,
    'index_de': index_de,
    'compter': compter,
    
    # Fonctions chaînes
    'majuscule': majuscule,
    'minuscule': minuscule,
    'remplacer': remplacer,
    'diviser': diviser,
    'joindre': joindre,
}
