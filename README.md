# F-IA - Langage de Programmation Français pour l'Intelligence Artificielle 🤖

**F-IA** est un langage de programmation en français spécialement conçu pour l'apprentissage et le développement d'applications d'intelligence artificielle.

## 🌟 Caractéristiques

- **Syntaxe française** intuitive et accessible
- **Support des caractères accentués** (é, è, à, ç, etc.)
- **Fonctions IA intégrées** (en cours de développement)
- **REPL interactif** pour l'expérimentation
- **Gestion d'erreurs avancée**

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

### Listes et accès indexé
```fia
soit fruits = ["pomme", "banane", "orange"]
imprimer(fruits[0])  # Affiche: pomme
fruits[1] = "poire"  # Modification
```

## 🛠️ Fonctions intégrées

- `imprimer(...)` - Affichage
- `longueur(objet)` - Taille d'une liste/chaîne
- `arrondir(nombre, décimales)` - Arrondi
- `aleatoire()` - Nombre aléatoire
- `racine(nombre)` - Racine carrée
- `puissance(base, exposant)` - Puissance
- `entier(valeur)` - Conversion en entier
- `chaine(valeur)` - Conversion en chaîne

## 🎯 Commandes REPL

- `.aide` - Afficher l'aide
- `.variables` - Lister les variables
- `.reset` - Réinitialiser l'environnement
- `.quitter` - Sortir du REPL

## 🤖 Fonctionnalités IA (à venir)

- `reseau_neuronal(couches, activation)` - Création de réseaux
- `apprentissage(modèle, données, époques)` - Entraînement
- `charger_jeu_de_donnees(chemin)` - Chargement de données

## 🐛 Signaler un bug

Ouvrez une issue sur GitHub avec :
- Code F-IA qui pose problème
- Message d'erreur complet
- Comportement attendu vs obtenu

## 📄 Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez CONTRIBUTING.md pour plus d'informations.
