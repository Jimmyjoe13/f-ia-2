# F-IA - Langage de Programmation Français pour l'Intelligence Artificielle 🤖

**F-IA** est un langage de programmation en français spécialement conçu pour l'apprentissage et le développement d'applications d'intelligence artificielle.

## 🌟 Caractéristiques

- **Syntaxe française** intuitive et accessible
- **Support des caractères accentués** (é, è, à, ç, etc.)
- **Dictionnaires natifs** avec accès par clé
- **Pipeline IA complet** intégré
- **REPL interactif** avec debug détaillé
- **Gestion d'erreurs avancée** avec localisation ligne/colonne
- **25+ fonctions intégrées** pour manipulation de données
- **🆕 Chatbot conversationnel** - Exemple d'application complète inclus
- **🆕 Support "sinon si"** - Syntaxe conditionnelle enrichie
- **🆕 Interaction utilisateur** - Fonctions `lire()` et `arreter()`

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

### 🤖 Démo Chatbot (NOUVEAU !)
```bash
python main.py exemples/chatbot_simple.fia
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

### Conditions avec "sinon si" 🆕
```fia
si (âge >= 18) {
    imprimer("Majeur")
} sinon si (âge >= 13) {
    imprimer("Adolescent")
} sinon {
    imprimer("Enfant")
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

## 🤖 Applications pratiques

### Chatbot conversationnel intelligent 🆕

F-IA permet de créer facilement des chatbots conversationnels :

```fia
fonction generer_reponse(message) {
    soit message_lower = minuscule(message)
    
    si (contient_mot(message_lower, "bonjour")) {
        retourner "Bonjour ! Comment puis-je vous aider aujourd'hui ?"
    } sinon si (contient_mot(message_lower, "merci")) {
        retourner "De rien ! Je suis ravi de pouvoir vous aider !"
    } sinon si (contient_mot(message_lower, "content")) {
        retourner "Je sens de la joie dans votre message ! C'est formidable ! 😊"
    } sinon {
        retourner "Intéressant ! Pouvez-vous m'en dire plus ? Je suis curieux d'apprendre !"
    }
}

# Boucle principale du chatbot
soit nom_bot = "F-IA Assistant"
soit compteur_messages = 0

imprimer("🤖", nom_bot, "v1.0")
imprimer("💬 Parlez-moi naturellement ou tapez /aide pour l'aide")

tant_que (vrai) {
    imprimer("Vous 💬 :")
    soit message_utilisateur = lire()
    
    si (message_utilisateur == "quitter") {
        imprimer("👋 Au revoir ! Merci d'avoir utilisé", nom_bot, "!")
        arreter()
    }
    
    soit reponse_bot = generer_reponse(message_utilisateur)
    imprimer("🤖", nom_bot, ":", reponse_bot)
    compteur_messages = compteur_messages + 1
}
```

### Pipeline IA intégré

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

### Fonctions d'interaction 🆕
- `lire()` - Lire une ligne depuis le clavier
- `arreter()` - Arrêter l'exécution proprement

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

### Chatbot avec système de commandes 🆕
```fia
fonction est_commande(message) {
    soit premier_mot = diviser(message, " ")[0]
    soit parties = diviser(premier_mot, "/")
    retourner longueur(parties) > 1
}

fonction traiter_commande(commande) {
    si (commande == "/aide") {
        imprimer("🤖 === AIDE F-IA ASSISTANT ===")
        imprimer("Commandes disponibles :")
        imprimer("/aide : Afficher cette aide")
        imprimer("/stats : Statistiques du bot")
        imprimer("Vous pouvez aussi me parler normalement !")
    } sinon si (commande == "/stats") {
        imprimer("📊 === STATISTIQUES ===")
        imprimer("Nom : F-IA Assistant")
        imprimer("Version : 1.0")
        imprimer("Mots-clés reconnus : 20+")
    }
}

# Application complète avec détection de commandes
tant_que (vrai) {
    soit message = lire()
    
    si (message == "quitter") {
        arreter()
    }
    
    si (est_commande(message)) {
        traiter_commande(message)
    } sinon {
        soit reponse = generer_reponse(message)
        imprimer("🤖 F-IA Assistant :", reponse)
    }
}
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
- **Gestion d'erreurs** (`errors.py`) - Système d'erreurs enrichi

## 🚀 Fonctionnalités avancées

- **Portée des variables** correcte avec pile de contextes
- **Gestion d'erreurs enrichie** avec ligne/colonne/fichier 🆕
- **Types de données** : entiers, flottants, chaînes, booléens, listes, dictionnaires
- **Opérateurs** : arithmétiques, comparaison, logiques, unaires
- **Accès mixte** : listes par index `[0]`, dictionnaires par clé `["nom"]`
- **Debugging intégré** : tokenisation et AST visibles dans le REPL
- **Syntaxe conditionnelle** : support complet de `sinon si` 🆕
- **Interaction utilisateur** : entrée clavier et arrêt contrôlé 🆕

## 🎮 Applications réalisables

Avec F-IA, vous pouvez créer :
- **🤖 Chatbots conversationnels** - Assistants virtuels intelligents
- **📊 Analyseurs de données** - Traitement et visualisation
- **🧠 Modèles d'IA** - Réseaux de neurones simples
- **🎯 Applications interactives** - Jeux, quizz, outils pédagogiques
- **📝 Outils de traitement de texte** - Analyse et transformation
- **🔢 Calculateurs avancés** - Statistiques et mathématiques

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

### ✅ Réalisé récemment
- [x] **Support "sinon si"** - Syntaxe conditionnelle enrichie
- [x] **Fonctions d'interaction** - `lire()` et `arreter()`
- [x] **Gestion d'erreurs avancée** - Messages avec ligne/colonne
- [x] **Chatbot fonctionnel** - Exemple d'application complète
- [x] **Correction bugs critiques** - ParseError et itération Bloc

### 🚧 Prochaines fonctionnalités
- [ ] Support des commentaires `# commentaire`
- [ ] Opérateurs d'assignation `+=`, `-=`, `*=`, `/=`
- [ ] Boucle `pour...dans` : `pour element dans liste`
- [ ] Classes et objets
- [ ] Système de modules et imports
- [ ] Intégration NumPy/TensorFlow réelle
- [ ] Gestionnaire de paquets
- [ ] Plus d'exemples de chatbots avancés

### 🔧 Améliorations techniques
- [ ] Compilation vers bytecode
- [ ] Optimisations de performance
- [ ] Language Server Protocol (LSP)
- [ ] Extension VSCode
- [ ] Documentation interactive
- [ ] Tests automatisés

---

**F-IA v0.3** - Créé avec ❤️ pour démocratiser l'IA en français

🏆 **Nouveau :** Chatbot conversationnel fonctionnel inclus ! Testez dès maintenant votre première application d'IA conversationnelle en français.