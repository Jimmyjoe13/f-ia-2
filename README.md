# F-IA - Langage de Programmation Français pour l'Intelligence Artificielle 🤖

**F-IA** est un langage de programmation en français spécialement conçu pour l'apprentissage et le développement d'applications d'intelligence artificielle.

## 🌟 Caractéristiques

- **Syntaxe française** intuitive et accessible
- **Support des caractères accentués** (é, è, à, ç, etc.)
- **Dictionnaires natifs** avec accès par clé
- **Pipeline IA complet** intégré
- **REPL interactif** avec debug détaillé
- **Gestion d'erreurs avancée** avec localisation
- **23 fonctions intégrées** pour manipulation de données

## 📦 Installation

```bash
git clone https://github.com/Jimmyjoe13/f-ia-2.git
cd f-ia-2
pip install -r requirements.txt
```

## 🚀 Utilisation

### Mode interactif (REPL)
```bash
python main.py
```

### Exécution de fichiers
```bash
python main.py mon_script.fia
```

## 📖 Syntaxe de base

### Variables et types
```fia
soit nom = "Alice"
soit âge = 25
soit notes = [15, 18, 12, 20]
soit actif = vrai
soit config = {"ville": "Paris", "pays": "France"}
```

### Dictionnaires
```fia
soit utilisateur = {"nom": "Alice", "age": 25, "ville": "Paris"}
imprimer(utilisateur["nom"])        # Alice
utilisateur["age"] = 26             # Modification
utilisateur["profession"] = "Dev"   # Ajout de clé
```

### Conditions
```fia
si (âge >= 18) {
    imprimer("Majeur")
} sinon {
    imprimer("Mineur")
}
```

### Boucles
```fia
# Boucle tant que
soit i = 0
tant_que (i < 5) {
    imprimer("Compteur:", i)
    i = i + 1
}

# Boucle pour
pour (soit j = 0; j < longueur(notes); j = j + 1) {
    imprimer("Note:", notes[j])
}
```

### Fonctions
```fia
fonction calculer_moyenne(liste_notes) {
    soit somme = 0
    soit i = 0
    tant_que (i < longueur(liste_notes)) {
        somme = somme + liste_notes[i]
        i = i + 1
    }
    retourner somme / longueur(liste_notes)
}

soit moyenne = calculer_moyenne([15, 18, 12, 20])
imprimer("Moyenne:", moyenne)
```

## 🤖 Pipeline IA intégré

```fia
# Création d'un réseau de neurones
soit modele = reseau_neuronal([2, 5, 1], "relu")

# Chargement de données
soit donnees = charger_jeu_de_donnees("iris")

# Entraînement
soit modele_entraine = apprentissage(modele, [[1, 2], [3, 4]], [0, 1], 50)

# Prédictions
soit predictions = prediction(modele_entraine, [[2, 3], [4, 5]])

# Évaluation
soit resultats = evaluer_modele(modele_entraine, [[1, 2]], [0])
imprimer("Précision:", resultats["precision"])
```

## 🛠️ Fonctions intégrées

### Fonctions de base
- `imprimer(...)` - Affichage
- `longueur(objet)` - Taille d'une liste/chaîne/dictionnaire
- `arrondir(nombre, décimales)` - Arrondi
- `aleatoire()` - Nombre aléatoire
- `racine(nombre)` - Racine carrée
- `puissance(base, exposant)` - Puissance
- `entier(valeur)` - Conversion en entier
- `chaine(valeur)` - Conversion en chaîne

### Fonctions dictionnaires
- `cles(dict)` - Liste des clés
- `valeurs(dict)` - Liste des valeurs
- `contient_cle(dict, cle)` - Vérifier l'existence d'une clé
- `supprimer_cle(dict, cle)` - Supprimer une clé
- `fusionner(dict1, dict2)` - Fusionner deux dictionnaires
- `vider(dict)` - Vider un dictionnaire

### Fonctions listes
- `ajouter(liste, element)` - Ajouter un élément
- `retirer(liste, index)` - Retirer un élément par index
- `trier(liste)` - Trier une liste
- `inverser(liste)` - Inverser l'ordre
- `copier(liste)` - Créer une copie
- `contient(liste, element)` - Vérifier la présence d'un élément
- `index_de(liste, element)` - Trouver l'index d'un élément
- `compter(liste, element)` - Compter les occurrences

### Fonctions chaînes
- `majuscule(texte)` - Convertir en majuscules
- `minuscule(texte)` - Convertir en minuscules
- `remplacer(texte, ancien, nouveau)` - Remplacer du texte
- `diviser(texte, separateur)` - Diviser en liste
- `joindre(liste, separateur)` - Joindre une liste en texte

### Fonctions IA
- `reseau_neuronal(couches, activation)` - Créer un réseau
- `apprentissage(modele, entrees, sorties, epoques)` - Entraîner
- `prediction(modele, donnees)` - Prédire
- `charger_jeu_de_donnees(nom)` - Charger des données
- `evaluer_modele(modele, test, vraies_sorties)` - Évaluer

## 🎯 Commandes REPL

- `.aide` - Afficher l'aide
- `.variables` - Lister les variables et fonctions
- `.reset` - Réinitialiser l'environnement
- `.quitter` - Sortir du REPL

## 📝 Exemples complets

### Manipulation de données
```fia
soit donnees = {"noms": ["Alice", "Bob", "Charlie"], "ages": [25, 30, 35]}
soit noms = donnees["noms"]
ajouter(noms, "Diana")
trier(noms)
imprimer("Noms triés:", noms)
```

### Traitement de texte
```fia
soit phrase = "Bonjour le monde F-IA"
soit mots = diviser(phrase, " ")
soit mots_maj = []
soit i = 0
tant_que (i < longueur(mots)) {
    ajouter(mots_maj, majuscule(mots[i]))
    i = i + 1
}
soit resultat = joindre(mots_maj, "-")
imprimer("Résultat:", resultat)  # BONJOUR-LE-MONDE-F-IA
```

### Machine Learning simple
```fia
# Données d'exemple pour classification binaire
soit donnees_x = [[0, 0], [0, 1], [1, 0], [1, 1]]
soit donnees_y = [0, 1, 1, 0]  # XOR

# Création et entraînement du modèle
soit reseau = reseau_neuronal([2, 4, 1], "relu")
soit modele_final = apprentissage(reseau, donnees_x, donnees_y, 100)

# Test du modèle
soit test_x = [[0, 0], [1, 1]]
soit predictions = prediction(modele_final, test_x)
imprimer("Prédictions XOR:", predictions)
```

## 🏗️ Architecture technique

F-IA est implémenté avec une architecture modulaire :
- **Lexer** (`lexer.py`) - Analyse lexicale et tokenisation
- **Parser** (`parser.py`) - Analyse syntaxique et génération d'AST
- **AST** (`fia_ast.py`) - Nœuds de l'arbre syntaxique abstrait  
- **Interpréteur** (`interpreter.py`) - Exécution du code
- **Fonctions intégrées** (`builtin.py`) - Bibliothèque standard
- **Module IA** (`ia_module.py`) - Fonctions d'intelligence artificielle
- **REPL** (`repl.py`) - Interface interactive

## 🚀 Fonctionnalités avancées

- **Portée des variables** correcte avec pile de contextes
- **Gestion d'erreurs** avec ligne/colonne/fichier
- **Types de données** : entiers, flottants, chaînes, booléens, listes, dictionnaires
- **Opérateurs** : arithmétiques, comparaison, logiques, unaires
- **Accès mixte** : listes par index `[0]`, dictionnaires par clé `["nom"]`
- **Debugging intégré** : tokenisation et AST visibles dans le REPL

## 🐛 Signaler un bug

Ouvrez une issue sur GitHub avec :
- Code F-IA qui pose problème
- Message d'erreur complet
- Comportement attendu vs obtenu
- Version de Python utilisée

## 📄 Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Commitez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 🎯 Roadmap

### Prochaines fonctionnalités
- [ ] Support des commentaires `# commentaire`
- [ ] Opérateurs d'assignation `+=`, `-=`, `*=`, `/=`
- [ ] Boucle `pour...dans` : `pour element dans liste`
- [ ] Classes et objets
- [ ] Système de modules et imports
- [ ] Intégration NumPy/TensorFlow réelle
- [ ] Gestionnaire de paquets

### Améliorations techniques
- [ ] Compilation vers bytecode
- [ ] Optimisations de performance
- [ ] Language Server Protocol (LSP)
- [ ] Extension VSCode
- [ ] Documentation interactive

---

**F-IA v0.2** - Créé avec ❤️ pour démocratiser l'IA en français