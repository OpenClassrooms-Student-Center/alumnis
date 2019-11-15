#!/usr/bin/python3 
# -*-coding: utf8 -*-

---


# FILENAME : celine-pelletier-2

# Example: https://openclassrooms.com/membres/celinemartinet

# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.

# lowercase, no blank space, Capital case or special character.

title: celine-pelletier-2


# First name or full name

name: Céline

date: 2019-11-06 21:05


# One line.

# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.

objective: Changer de métier, pour être plus épanouie.

short_description: J'aime les jeux vidéos, le dessin et l'équitation.


# don't touch that

template: students

description:

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod

    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,

    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo

    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse

    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non

    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


# image must be located in content/images/students

# name should be the same as this file. Eg: celinemartinet.png

image: celine.png


# Change this to True when you do you pull request.

public: True


# You need to keep the exact same structure for each new project.

projects:

  - title: Présentez-vous !

    description: Je m'appelle Céline, j'ai 25 ans et j'habite en région parisienne. https://www.linkedin.com/in/céline-pelletier-585170192

    # Create a new repository for your images. Name it the same as your nickname and profile picture.

    # Image must be here: content/students/yourrepo/project1.png

    image: celine-pelletier-2/projet1.png

    link: http://www.ricochet-jeunes.org/auteurs/recherche/10146-olivier-vogel

    # 'true' makes it fully available.

    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!

    finished: true

  - title: Intégrez la communauté !

    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 

    image: celine-pelletier-2/projet2.png

    link: https://openclassrooms-student-center.github.io/presentation/students/ratus.html

    finished: true

  - title: Aidez MacGyver à sortir !

    description: Création d’un jeu développé en Python et utilisant PyGame.

    image: celine-pelletier-2/projet_3.png

    link: https://www.github.com

    finished: false

---
