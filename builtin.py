# builtin.py
from errors import RuntimeError

def _imprimer(*args):
    # Supporte l'affichage de plusieurs arguments comme print
    print(*args)

def _longueur(obj):
    try:
        return len(obj)
    except Exception:
        raise RuntimeError("Erreur d'exécution: 'longueur' attend une liste, chaîne ou dictionnaire")

def _arrondir(nombre, decimales=0):
    try:
        return round(float(nombre), int(decimales))
    except Exception:
        raise RuntimeError("Erreur d'exécution: 'arrondir' attend (nombre, décimales)")

def _aleatoire():
    import random
    return random.random()

def _racine(nombre):
    import math
    try:
        return math.sqrt(float(nombre))
    except Exception:
        raise RuntimeError("Erreur d'exécution: 'racine' attend un nombre")

def _puissance(base, exposant):
    try:
        return float(base) ** float(exposant)
    except Exception:
        raise RuntimeError("Erreur d'exécution: 'puissance' attend (base, exposant)")

def _entier(valeur):
    try:
        if isinstance(valeur, bool):
            return int(valeur)
    except Exception:
        pass
    try:
        return int(valeur)
    except Exception:
        raise RuntimeError("Erreur d'exécution: 'entier' ne peut pas convertir cette valeur")

def _chaine(valeur):
    try:
        return str(valeur)
    except Exception:
        raise RuntimeError("Erreur d'exécution: 'chaine' ne peut pas convertir cette valeur")

# Dictionnaires
def _cles(d):
    if not isinstance(d, dict):
        raise RuntimeError("Erreur d'exécution: 'cles' attend un dictionnaire")
    return list(d.keys())

def _valeurs(d):
    if not isinstance(d, dict):
        raise RuntimeError("Erreur d'exécution: 'valeurs' attend un dictionnaire")
    return list(d.values())

def _contient_cle(d, cle):
    if not isinstance(d, dict):
        raise RuntimeError("Erreur d'exécution: 'contient_cle' attend un dictionnaire")
    return cle in d

def _supprimer_cle(d, cle):
    if not isinstance(d, dict):
        raise RuntimeError("Erreur d'exécution: 'supprimer_cle' attend un dictionnaire")
    d.pop(cle, None)
    return d

def _fusionner(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise RuntimeError("Erreur d'exécution: 'fusionner' attend deux dictionnaires")
    r = d1.copy()
    r.update(d2)
    return r

def _vider(d):
    if not isinstance(d, dict):
        raise RuntimeError("Erreur d'exécution: 'vider' attend un dictionnaire")
    d.clear()
    return d

# Listes
def _ajouter(l, e):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'ajouter' attend une liste")
    l.append(e)
    return l

def _retirer(l, index):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'retirer' attend une liste")
    if not isinstance(index, int) or index < 0 or index >= len(l):
        raise RuntimeError("Erreur d'exécution: index invalide dans 'retirer'")
    l.pop(index)
    return l

def _trier(l):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'trier' attend une liste")
    try:
        l.sort()
    except Exception:
        raise RuntimeError("Erreur d'exécution: la liste ne peut pas être triée")
    return l

def _inverser(l):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'inverser' attend une liste")
    l.reverse()
    return l

def _copier(l):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'copier' attend une liste")
    return l.copy()

def _contient(l, e):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'contient' attend une liste")
    return e in l

def _index_de(l, e):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'index_de' attend une liste")
    try:
        return l.index(e)
    except ValueError:
        return -1

def _compter(l, e):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'compter' attend une liste")
    return l.count(e)

# Chaînes
def _majuscule(t):
    if not isinstance(t, str):
        raise RuntimeError("Erreur d'exécution: 'majuscule' attend une chaîne")
    return t.upper()

def _minuscule(t):
    if not isinstance(t, str):
        raise RuntimeError("Erreur d'exécution: 'minuscule' attend une chaîne")
    return t.lower()

def _remplacer(t, ancien, nouveau):
    if not isinstance(t, str):
        raise RuntimeError("Erreur d'exécution: 'remplacer' attend une chaîne")
    return t.replace(str(ancien), str(nouveau))

def _diviser(t, sep):
    if not isinstance(t, str):
        raise RuntimeError("Erreur d'exécution: 'diviser' attend une chaîne")
    return t.split(str(sep))

def _joindre(l, sep):
    if not isinstance(l, list):
        raise RuntimeError("Erreur d'exécution: 'joindre' attend une liste")
    return str(sep).join(str(x) for x in l)

# I/O utilisateur
def _lire():
    try:
        return input()
    except EOFError:
        return ""
    except Exception as e:
        raise RuntimeError(f"Erreur d'exécution: 'lire' a échoué: {e}")

# Arrêt contrôlé
class _ArretProgramme(Exception):
    pass

def _arreter():
    # Cette fonction peut être interceptée par l'interpréteur si besoin
    raise _ArretProgramme()

# === NOUVELLES FONCTIONS IA ===
# Import avec gestion d'erreur pour les dépendances IA
def _safe_import_ai():
    """Import sécurisé du module IA"""
    try:
        from ai_integration import (
            _appeler_ia, _lister_plateformes_ia, _lister_modeles_ia, 
            _generer_reponse_bot, _verifier_config_ia
        )
        return {
            'appeler_ia': _appeler_ia,
            'lister_plateformes_ia': _lister_plateformes_ia,
            'lister_modeles_ia': _lister_modeles_ia,
            'generer_reponse_bot': _generer_reponse_bot,
            'verifier_config_ia': _verifier_config_ia
        }
    except ImportError as e:
        # Si les dépendances IA ne sont pas installées
        def _ia_non_disponible(*args, **kwargs):
            raise RuntimeError("Fonctions IA non disponibles. Installez les dépendances: pip install -r requirements.txt")
        
        return {
            'appeler_ia': _ia_non_disponible,
            'lister_plateformes_ia': _ia_non_disponible,
            'lister_modeles_ia': _ia_non_disponible,
            'generer_reponse_bot': _ia_non_disponible,
            'verifier_config_ia': _ia_non_disponible
        }
    except Exception as e:
        # Autres erreurs (clés API manquantes, etc.)
        def _ia_erreur(*args, **kwargs):
            raise RuntimeError(f"Erreur IA: {str(e)}")
        
        return {
            'appeler_ia': _ia_erreur,
            'lister_plateformes_ia': _ia_erreur,
            'lister_modeles_ia': _ia_erreur,
            'generer_reponse_bot': _ia_erreur,
            'verifier_config_ia': _ia_erreur
        }

# Charger les fonctions IA
_ai_functions = _safe_import_ai()

# Table des fonctions intégrées exposées au langage F-IA
FONCTIONS_INTEGREES = {
    # Fonctions de base
    "imprimer": _imprimer,
    "longueur": _longueur,
    "arrondir": _arrondir,
    "aleatoire": _aleatoire,
    "racine": _racine,
    "puissance": _puissance,
    "entier": _entier,
    "chaine": _chaine,

    # Dictionnaires
    "cles": _cles,
    "valeurs": _valeurs,
    "contient_cle": _contient_cle,
    "supprimer_cle": _supprimer_cle,
    "fusionner": _fusionner,
    "vider": _vider,

    # Listes
    "ajouter": _ajouter,
    "retirer": _retirer,
    "trier": _trier,
    "inverser": _inverser,
    "copier": _copier,
    "contient": _contient,
    "index_de": _index_de,
    "compter": _compter,

    # Chaînes
    "majuscule": _majuscule,
    "minuscule": _minuscule,
    "remplacer": _remplacer,
    "diviser": _diviser,
    "joindre": _joindre,

    # I/O utilisateur
    "lire": _lire,
    "arreter": _arreter,

    # === FONCTIONS IA INTÉGRÉES ===
    "appeler_ia": _ai_functions['appeler_ia'],
    "lister_plateformes_ia": _ai_functions['lister_plateformes_ia'],
    "lister_modeles_ia": _ai_functions['lister_modeles_ia'],
    "generer_reponse_bot": _ai_functions['generer_reponse_bot'],
    "verifier_config_ia": _ai_functions['verifier_config_ia'],
}
