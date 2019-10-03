---

# FILENAME : lewyl7
# Example: https://openclassrooms.com/membres/larry-yala
# lowercase, no blank space, Capital case or special character.
title: larry.md

# First name or full name
name: larry
date: 2018-10-07 21:06

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: créer ma propre application
short_description: J'aime le football et passer du temps en famille, je suis motivé à reussir. J'apprend à coder pour etre autonome

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
image: larry.jpg

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: 30 ans, marié et un enfant, j'ai soif d'apprendre pour atteindre mes objectifs
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: ratus/projet_1.png
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: ratus/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/ratus.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    finished: false
---

