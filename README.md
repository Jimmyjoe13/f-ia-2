# F-IA - Langage de Programmation Français pour l'Intelligence Artificielle 🤖

**F-IA** est un langage de programmation en français spécialement conçu pour l'apprentissage et le développement d'applications d'intelligence artificielle.

## 🌟 Caractéristiques

- **Syntaxe française** intuitive et accessible
- **Support des caractères accentués** (é, è, à, ç, etc.)
- **Dictionnaires natifs** avec accès par clé
- **Pipeline IA complet** intégré
- **REPL interactif** avec debug détaillé
- **Gestion d'erreurs avancée** avec localisation ligne/colonne
- **30+ fonctions intégrées** pour manipulation de données
- **🔥 IA générative intégrée** - OpenAI GPT-5, GPT-4.1, DeepSeek
- **🆕 Chatbot conversationnel** - Exemple d'application complète inclus
- **🆕 Support "sinon si"** - Syntaxe conditionnelle enrichie
- **🆕 Interaction utilisateur** - Fonctions `lire()` et `arreter()`

## 📦 Installation

```bash
git clone https://github.com/Jimmyjoe13/f-ia-2.git
cd f-ia-2
pip install -r requirements.txt
```

## ⚙️ Configuration IA

Créez un fichier `.env` à la racine du projet :
```env
OPENAI_API_KEY=votre_cle_openai_ici
DEEPSEEK_API_KEY=votre_cle_deepseek_ici
DEFAULT_AI_MODEL=gpt-4.1-nano
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

### 🤖 Démo Chatbot Simple
```bash
python main.py chatbot_simple.fia
```

### 🔥 Démo Chatbot IA Avancé (NOUVEAU !)
```bash
python main.py chatbot_ia_avance.fia
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

## 🔥 Intégration IA Générative (NOUVEAU !)

### Appel direct aux IA
```fia
# Appeler OpenAI GPT-5
soit reponse = appeler_ia("openai", "gpt-5", "Explique-moi la programmation")
imprimer("GPT-5:", reponse)

# Appeler DeepSeek
soit code = appeler_ia("deepseek", "deepseek-coder", "Écris une fonction de tri en Python")
imprimer("DeepSeek:", code)

# Générer une réponse de chatbot optimisée
soit reponse_bot = generer_reponse_bot(
    "openai", 
    "gpt-4.1-nano", 
    "Bonjour comment ça va ?",
    "Tu es un assistant sympa et serviable"
)
imprimer("Bot:", reponse_bot)
```

### Gestion des plateformes IA
```fia
# Vérifier les plateformes configurées
soit config = verifier_config_ia()
imprimer("OpenAI:", config["openai"])
imprimer("DeepSeek:", config["deepseek"])

# Lister les plateformes disponibles
soit plateformes = lister_plateformes_ia()
imprimer("Plateformes:", plateformes)  # ['openai', 'deepseek']

# Lister les modèles OpenAI
soit modeles = lister_modeles_ia("openai")
imprimer("Modèles OpenAI:", modeles)
# ['gpt-5', 'gpt-5-mini', 'gpt-5-nano', 'gpt-4.1', 'gpt-4.1-mini', 'gpt-4.1-nano', ...]
```

## 🤖 Applications pratiques

### Chatbot IA conversationnel 🔥
```fia
imprimer("🤖 Chatbot F-IA avec IA Générative")

# Configuration automatique
soit plateformes = lister_plateformes_ia()
soit plateforme = plateformes[0]
soit modele = "gpt-4.1-nano"

si (plateforme == "deepseek") {
    modele = "deepseek-chat"
}

# Boucle conversationnelle
tant_que (vrai) {
    imprimer("👤 Vous:")
    soit message = lire()
    
    si (message == "quitter") {
        arreter()
    }
    
    # Génération de réponse par IA
    soit reponse = generer_reponse_bot(
        plateforme,
        modele,
        message,
        "Tu es un assistant intelligent créé avec F-IA"
    )
    
    imprimer("🤖 Assistant:", reponse)
}
```

### Pipeline IA traditionnel
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

### Fonctions IA générative 🔥
- `appeler_ia(plateforme, modele, message)` - Appel direct à une IA
- `generer_reponse_bot(plateforme, modele, message, contexte)` - Réponse de chatbot optimisée
- `lister_plateformes_ia()` - Plateformes IA configurées
- `lister_modeles_ia(plateforme)` - Modèles disponibles par plateforme
- `verifier_config_ia()` - Vérifier la configuration IA

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

### Fonctions IA (réseau neuronal)
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

## 🔥 Plateformes IA supportées

### OpenAI (Octobre 2025)
- **GPT-5** (dernière génération) 🆕
  - `gpt-5` - Modèle complet ultra-performant
  - `gpt-5-mini` - Version équilibrée
  - `gpt-5-nano` - Version ultra-rapide
- **GPT-4.1** (Avril 2025)
  - `gpt-4.1` - Modèle complet optimisé code
  - `gpt-4.1-mini` - Version équilibrée
  - `gpt-4.1-nano` - Version économique (recommandé)
- **GPT-4o** (Legacy)
  - `gpt-4o`, `gpt-4o-mini`

### DeepSeek
- `deepseek-chat` - Conversation générale
- `deepseek-coder` - Spécialisé programmation
- `deepseek-v3` - Dernière version

## 📝 Exemples complets

### Chatbot multi-IA avec sélection de modèle 🔥
```fia
imprimer("🤖 === CHATBOT MULTI-IA F-IA ===")

soit plateformes = lister_plateformes_ia()
imprimer("Plateformes disponibles:", plateformes)

# Choisir OpenAI par défaut si disponible
soit plateforme_active = plateformes[0]
soit modele_actif = "gpt-4.1-nano"

si (plateforme_active == "deepseek") {
    modele_actif = "deepseek-chat"
}

imprimer("🎯 Utilisation:", plateforme_active, "avec", modele_actif)

fonction changer_ia() {
    imprimer("Plateformes disponibles:")
    soit i = 0
    tant_que (i < longueur(plateformes)) {
        imprimer("  ", i + 1, ".", plateformes[i])
        i = i + 1
    }
    imprimer("Choisir (1-", longueur(plateformes), ") :")
    soit choix = lire()
    
    si (choix == "1") {
        plateforme_active = plateformes[0]
        si (plateforme_active == "openai") {
            modele_actif = "gpt-4.1-nano"
        } sinon si (plateforme_active == "deepseek") {
            modele_actif = "deepseek-chat"
        }
        imprimer("✅ Changé pour:", plateforme_active, "avec", modele_actif)
    }
}

# Boucle principale
tant_que (vrai) {
    imprimer("\n👤 Vous (tapez /ia pour changer d'IA):")
    soit message = lire()
    
    si (message == "quitter") {
        imprimer("👋 Au revoir !")
        arreter()
    } sinon si (message == "/ia") {
        changer_ia()
    } sinon {
        imprimer("🤖 Génération par", plateforme_active, "...")
        soit reponse = generer_reponse_bot(
            plateforme_active,
            modele_actif,
            message,
            "Tu es un assistant IA créé avec le langage F-IA. Réponds en français."
        )
        imprimer("🔥", plateforme_active.majuscule(), ":", reponse)
    }
}
```

### Générateur de code avec IA 🔥
```fia
imprimer("💻 === GÉNÉRATEUR DE CODE F-IA ===")

fonction generer_code(langage, description) {
    soit prompt = joindre([
        "Génère du code", langage, "pour:", description,
        "\nRéponds seulement avec le code, sans explication."
    ], " ")
    
    # Utiliser DeepSeek si disponible (spécialisé code)
    soit plateformes = lister_plateformes_ia()
    soit plateforme = "openai"
    soit modele = "gpt-4.1-nano"
    
    si (contient(plateformes, "deepseek")) {
        plateforme = "deepseek"
        modele = "deepseek-coder"
    }
    
    retourner appeler_ia(plateforme, modele, prompt)
}

# Interface utilisateur
tant_que (vrai) {
    imprimer("\n💻 Générateur de Code IA")
    imprimer("Langage (Python, JavaScript, etc.) :")
    soit langage = lire()
    
    si (langage == "quitter") {
        arreter()
    }
    
    imprimer("Description de la fonction :")
    soit description = lire()
    
    imprimer("🤖 Génération du code", langage, "...")
    soit code = generer_code(langage, description)
    
    imprimer("✨ Code généré:")
    imprimer("```" + minuscule(langage))
    imprimer(code)
    imprimer("```")
}
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
- **Intégration IA** (`ai_integration.py`) - OpenAI, DeepSeek, etc. 🔥
- **Configuration IA** (`ai_config.py`) - Gestion des clés API 🔥
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
- **IA générative native** : intégration OpenAI et DeepSeek 🔥

## 🎮 Applications réalisables

Avec F-IA, vous pouvez créer :
- **🔥 Chatbots IA avancés** - GPT-5, GPT-4.1, DeepSeek intégrés
- **💻 Générateurs de code IA** - Assistants de programmation
- **📚 Assistants éducatifs** - Tuteurs IA personnalisés  
- **🤖 Agents conversationnels** - Support client automatisé
- **📊 Analyseurs de données IA** - Traitement intelligent
- **🧠 Modèles d'IA hybrides** - Combinaison ML classique + IA générative
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
- [x] **Intégration IA générative** - OpenAI GPT-5, GPT-4.1, DeepSeek 🔥
- [x] **5 nouvelles fonctions IA** - Appels directs aux plateformes
- [x] **Chatbot IA avancé** - Changement dynamique de modèles
- [x] **Support multi-plateformes** - Configuration automatique
- [x] **Support "sinon si"** - Syntaxe conditionnelle enrichie
- [x] **Fonctions d'interaction** - `lire()` et `arreter()`
- [x] **Gestion d'erreurs avancée** - Messages avec ligne/colonne
- [x] **Correction bugs critiques** - ParseError et itération Bloc

### 🚧 Prochaines fonctionnalités
- [ ] Support des commentaires `# commentaire`
- [ ] Opérateurs d'assignation `+=`, `-=`, `*=`, `/=`
- [ ] Boucle `pour...dans` : `pour element dans liste`
- [ ] Intégration Claude (Anthropic)
- [ ] Génération d'images IA (DALL-E, Midjourney)
- [ ] Système de RAG (Retrieval-Augmented Generation)
- [ ] Classes et objets
- [ ] Système de modules et imports
- [ ] Gestionnaire de paquets
- [ ] Plus d'exemples IA (agents, workflows)

### 🔧 Améliorations techniques
- [ ] Compilation vers bytecode
- [ ] Optimisations de performance
- [ ] Language Server Protocol (LSP)
- [ ] Extension VSCode avec support IA
- [ ] Documentation interactive
- [ ] Tests automatisés
- [ ] Interface web (F-IA en ligne)

---

**F-IA v1.0** - Créé avec ❤️ pour démocratiser l'IA en français

🔥 **RÉVOLUTIONNAIRE :** Premier langage de programmation français avec IA générative native ! Créez des chatbots, générateurs de code et assistants IA en quelques lignes !