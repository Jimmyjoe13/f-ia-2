# ia_module.py
from errors import RuntimeError
import random
import math

def reseau_neuronal(couches, activation="relu"):
    """
    Crée un réseau de neurones simple.
    Args:
        couches: Liste des nombres de neurones par couche [entrée, cachée, sortie]
        activation: Type d'activation ('relu', 'sigmoid', 'tanh')
    """
    if not isinstance(couches, list) or len(couches) < 2:
        raise RuntimeError("Le paramètre 'couches' doit être une liste d'au moins 2 éléments")
    
    activations_supportees = ['relu', 'sigmoid', 'tanh']
    if activation not in activations_supportees:
        raise RuntimeError(f"Activation '{activation}' non supportée. Utilisez: {activations_supportees}")
    
    # Génération des poids aléatoires
    poids = []
    for i in range(len(couches) - 1):
        poids_couche = []
        for j in range(couches[i]):
            neurone_poids = [random.uniform(-1, 1) for _ in range(couches[i + 1])]
            poids_couche.append(neurone_poids)
        poids.append(poids_couche)
    
    reseau = {
        "type": "reseau_neuronal",
        "architecture": couches,
        "activation": activation,
        "poids": poids,
        "entraine": False,
        "precision": 0.0
    }
    
    print(f"✅ Réseau créé - Architecture: {couches}, Activation: {activation}")
    return reseau

def apprentissage(modele, donnees_entrees, donnees_sorties, epoques=100, taux_apprentissage=0.01):
    """
    Entraîne un modèle sur des données.
    Args:
        modele: Réseau de neurones créé avec reseau_neuronal()
        donnees_entrees: Liste des exemples d'entrée
        donnees_sorties: Liste des résultats attendus
        epoques: Nombre d'itérations d'entraînement
        taux_apprentissage: Vitesse d'apprentissage
    """
    if not isinstance(modele, dict) or modele.get("type") != "reseau_neuronal":
        raise RuntimeError("Le modèle doit être créé avec 'reseau_neuronal()'")
    
    if not isinstance(donnees_entrees, list) or not isinstance(donnees_sorties, list):
        raise RuntimeError("Les données d'entrée et de sortie doivent être des listes")
    
    if len(donnees_entrees) != len(donnees_sorties):
        raise RuntimeError("Le nombre d'exemples d'entrée et de sortie doit être identique")
    
    print(f"📊 Début de l'entraînement sur {len(donnees_entrees)} exemples")
    print(f"⏱️ {epoques} époques à un taux de {taux_apprentissage}")
    
    # Simulation d'entraînement
    erreur_initiale = 1.0
    for epoque in range(epoques):
        # Calcul de l'erreur simulée (décroîlt avec les époques)
        erreur = erreur_initiale * math.exp(-epoque / (epoques / 4))
        
        # Affichage du progrès tous les 20%
        if epoque % max(1, epoques // 5) == 0:
            print(f"Époque {epoque + 1}/{epoques} - Erreur: {erreur:.4f}")
    
    # Calcul d'une précision simulée
    precision_finale = min(0.95, 0.5 + (epoques / 200))
    modele["entraine"] = True
    modele["precision"] = precision_finale
    
    print(f"✅ Entraînement terminé - Précision: {precision_finale:.2%}")
    return modele

def prediction(modele, donnees_test):
    """
    Effectue des prédictions avec un modèle entraîné.
    Args:
        modele: Modèle entraîné
        donnees_test: Données à prédire
    """
    if not isinstance(modele, dict) or not modele.get("entraine", False):
        raise RuntimeError("Le modèle doit être entraîné avant la prédiction")
    
    if not isinstance(donnees_test, list):
        raise RuntimeError("Les données de test doivent être une liste")
    
    # Génération de prédictions simulées
    predictions = []
    for i, exemple in enumerate(donnees_test):
        # Prédiction aléatoire pondérée par la précision du modèle
        base = sum(exemple) if isinstance(exemple, list) else exemple
        bruit = random.uniform(-0.1, 0.1) * (1 - modele["precision"])
        pred = abs(base + bruit) % 2  # Simulation d'une classification binaire
        predictions.append(round(pred))
    
    print(f"🎯 Prédictions générées pour {len(donnees_test)} exemples")
    return predictions

def charger_jeu_de_donnees(chemin):
    """
    Charge et prépare un jeu de données depuis un fichier.
    Args:
        chemin: Chemin vers le fichier de données
    """
    if not isinstance(chemin, str):
        raise RuntimeError("Le chemin doit être une chaîne de caractères")
    
    try:
        # Simulation de chargement avec données factices
        if "iris" in chemin.lower():
            donnees = {
                "nom": "Iris Dataset",
                "exemples": 150,
                "caracteristiques": ["longueur_sepale", "largeur_sepale", "longueur_petale", "largeur_petale"],
                "classes": ["setosa", "versicolor", "virginica"],
                "donnees_entrees": [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]],
                "donnees_sorties": [0, 0, 2]
            }
        elif "digits" in chemin.lower():
            donnees = {
                "nom": "Digits Dataset",
                "exemples": 1797,
                "caracteristiques": [f"pixel_{i}" for i in range(64)],
                "classes": list(range(10)),
                "donnees_entrees": [[0] * 64 for _ in range(3)],  # Images 8x8 pixels
                "donnees_sorties": [0, 1, 2]
            }
        else:
            # Jeu de données générique
            donnees = {
                "nom": f"Dataset from {chemin}",
                "exemples": 100,
                "caracteristiques": ["feature_1", "feature_2"],
                "classes": ["classe_A", "classe_B"],
                "donnees_entrees": [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(5)],
                "donnees_sorties": [random.randint(0, 1) for _ in range(5)]
            }
        
        print(f"📁 Jeu de données chargé: {donnees['nom']}")
        print(f"📊 {donnees['exemples']} exemples, {len(donnees['caracteristiques'])} caractéristiques")
        print(f"🏷️ Classes: {donnees['classes']}")
        
        return donnees
        
    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement de {chemin}: {e}")

def evaluer_modele(modele, donnees_test, vraies_sorties):
    """
    Évalue les performances d'un modèle.
    Args:
        modele: Modèle entraîné
        donnees_test: Données de test
        vraies_sorties: Vraies étiquettes
    """
    predictions = prediction(modele, donnees_test)
    
    if len(predictions) != len(vraies_sorties):
        raise RuntimeError("Le nombre de prédictions et de vraies sorties doit être identique")
    
    # Calcul de la précision
    corrects = sum(1 for p, v in zip(predictions, vraies_sorties) if p == v)
    precision = corrects / len(vraies_sorties)
    
    # Statistiques
    resultats = {
        "precision": precision,
        "predictions_correctes": corrects,
        "total_predictions": len(predictions),
        "erreur": 1 - precision
    }
    
    print(f"📊 Résultats de l'évaluation:")
    print(f"✅ Précision: {precision:.2%}")
    print(f"🎯 {corrects}/{len(vraies_sorties)} prédictions correctes")
    print(f"❌ Taux d'erreur: {(1-precision):.2%}")
    
    return resultats

# Dictionnaire des fonctions IA intégrées
FONCTIONS_IA = {
    'reseau_neuronal': reseau_neuronal,
    'apprentissage': apprentissage,
    'prediction': prediction,
    'charger_jeu_de_donnees': charger_jeu_de_donnees,
    'evaluer_modele': evaluer_modele,
}