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
- **🔥 IA générative intégrée** - OpenAI GPT-5 / GPT-4.1 / DeepSeek
- **🆕 Chatbot conversationnel** - Exemples complets inclus
- **🆕 Support "sinon si"** - Syntaxe conditionnelle enrichie
- **🆕 Interaction utilisateur** - Fonctions `lire()` et `arreter()`
- **🆕 Commentaires** - `# ...` et `// ...` (ligne)
- **🆕 Opérateurs d'assignation** - `+=`, `-=`, `*=`, `/=`, `%=`

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

### 🔥 Démo Chatbot IA Avancé
```bash
python main.py chatbot_ia_avance.fia
```

## ✨ Nouveautés récentes

- **Commentaires ligne**: `#` et `//` ignorés jusqu'à fin de ligne
- **Opérateurs d'assignation composés**: `+=`, `-=`, `*=`, `/=`, `%=`
- **Exemple de test**: `exemples/test_op_compose.fia`

```fia
soit x = 10
x += 5
imprimer("x:", x)
x -= 2
imprimer("x:", x)
x *= 3
imprimer("x:", x)
x /= 13
imprimer("x:", x)
x %= 2
imprimer("x:", x)
```

Sortie attendue:
```
x: 15
x: 13
x: 39
x: 3.0
x: 1.0
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

### Conditions avec "sinon si"
```fia
si (âge >= 18) {
    imprimer("Majeur")
} sinon si (âge >= 13) {
    imprimer("Adolescent")
} sinon {
    imprimer("Enfant")
}
```

### Boucles (classique)
```fia
# Boucle tant que
soit i = 0
tant_que (i < 5) {
    imprimer("Compteur:", i)
    i = i + 1
}

# Boucle pour (style C)
pour (soit j = 0; j < longueur(notes); j = j + 1) {
    imprimer("Note:", notes[j])
}
```

## 🔥 Intégration IA Générative

### Appel direct aux IA
```fia
soit reponse = appeler_ia("openai", "gpt-4.1-nano", "Explique-moi la programmation")
imprimer("OpenAI:", reponse)

soit code = appeler_ia("deepseek", "deepseek-coder", "Écris une fonction de tri en Python")
imprimer("DeepSeek:", code)
```

### Générer une réponse de chatbot
```fia
soit reponse_bot = generer_reponse_bot(
    "openai",
    "gpt-4.1-nano",
    "Bonjour comment ça va ?",
    "Tu es un assistant sympa et serviable"
)
imprimer("Bot:", reponse_bot)
```

## 🏗️ Architecture technique

- **Lexer** (`lexer.py`) - Analyse lexicale (inclut commentaires `#` et `//`)
- **Parser** (`parser.py`) - Analyse syntaxique (assignations composées)
- **AST** (`fia_ast.py`) - Nœuds de syntaxe (AssignationComposee, etc.)
- **Interpréteur** (`interpreter.py`) - Exécution (support `+=`, `-=`, ...)
- **Fonctions intégrées** (`builtin.py`) - Bibliothèque standard
- **Module IA** (`ia_module.py`) - Fonctions d'intelligence artificielle
- **Intégration IA** (`ai_integration.py`) - OpenAI, DeepSeek
- **REPL** (`repl.py`) - Interface interactive
- **Gestion d'erreurs** (`errors.py`) - Système d'erreurs enrichi

## 🗺️ Roadmap (prochaines étapes)

- **Boucle `pour...dans`**: `pour nom dans noms { ... }`
- **Conversion robuste**: `entier()` et conversions sûres
- **Support Anthropic (Claude)**
- **Génération d'images** (DALL-E / Stable Diffusion)
- **Système de modules / imports**

---

**F-IA v1.1** - IA générative native, commentaires, et opérateurs d'assignation 🚀
