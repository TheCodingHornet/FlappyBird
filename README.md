# Flappy Bird avec PyGame

Ce dépôt contient une implémentation du jeu **Flappy Bird** réalisée en Python à l’aide de la bibliothèque **PyGame**. Le principe du jeu est simple : contrôler un oiseau qui doit franchir des passages entre des tuyaux sans entrer en collision avec ces derniers ou avec le sol/plafond.

## Sommaire
1. [Caractéristiques](#caractéristiques)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Structure du projet](#structure-du-projet)
6. [Contribuer](#contribuer)
7. [Licence](#licence)
8. [Auteurs](#auteurs)

---

## Caractéristiques
- **Défilement du fond** et du sol en continu pour donner une impression de mouvement.
- **Gestion de la gravité** et du mouvement de l’oiseau via la variable `bird_movement`.
- **Génération aléatoire** des tuyaux avec des positions et des espaces aléatoires.
- **Système de score** incrémenté en continu à mesure que le joueur reste en vie.
- **Écrans de démarrage et de fin** (Game Over) avec affichage du score.

---

## Prérequis
- **Python 3.7+** (de préférence la dernière version stable).
- **PyGame** (version 2.0 ou supérieure conseillée).

Pour vérifier que PyGame est installé, vous pouvez utiliser la commande suivante dans un terminal :

```bash
pip show pygame
```

Si PyGame n’est pas installé, veuillez exécuter :

```bash
pip install pygame
```

---

## Installation
1. **Cloner** ce dépôt ou téléchargez-le au format ZIP :
   ```bash
   git clone https://github.com/TheCodingHornet/FlappyBird.git
   ```
2. **Accéder** au répertoire du projet :
   ```bash
   cd FlappyBird
   ```
3. **Installer** PyGame (si nécessaire) :
   ```bash
   pip install pygame
   ```

---

## Utilisation
1. Placez-vous à la racine du projet (là où se trouve le fichier `.py`).
2. Lancez le script principal :
   ```bash
   python FlappyBird.py
   ```
3. **Contrôles du jeu** :
   - Appuyez sur la **barre d’espace** pour :
     - Lancer la partie.
     - Faire sauter l’oiseau lorsque la partie est en cours.
     - Relancer la partie après un Game Over.

---

## Structure du projet

```
FlappyBird/
├── assets/
│   ├── background.png
│   ├── ground.png
│   ├── pipe.png
│   ├── bird1.png
│   ├── bird2.png
│   └── bird3.png
└── FlappyBird.py
```

- **assets/** : Contient les ressources graphiques (fond, sol, tuyau, sprites de l’oiseau).
- **FlappyBird.py** : Point d’entrée du jeu. Gère l’initialisation de PyGame, la boucle principale et toutes les mécaniques de Flappy Bird.

---

## Contribuer
Les contributions sont les bienvenues. Veuillez :
1. **Forker** le dépôt.
2. **Créer une branche** dédiée à votre fonctionnalité ou correction de bug.
3. **Ajouter** vos modifications et **committer** vos changements.
4. **Proposer une Pull Request** pour revue.

---

## Licence
Ce projet est distribué sous la licence [MIT](https://opensource.org/licenses/MIT). Vous êtes libre de l’utiliser, de le modifier et de le redistribuer. Veillez à respecter les termes de la licence lors de toute redistribution du code.

---

## Auteurs
- **Simon Stephan / TheCodingHornet** : Créateur du projet et implémentation du code.

Pour toute question ou suggestion, n’hésitez pas à ouvrir une [issue](https://github.com/TheCodingHornet/FlappyBird/issues) sur ce dépôt ou à me contacter directement.

