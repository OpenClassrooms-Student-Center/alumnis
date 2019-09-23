---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: salima

# First name or full name
name: Salima
date: 2018-10-18 11:03

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Devenir développeuse Android.
short_description: J'aime les voyages en sac à dos, la photographie, le théâtre et le digital. J'apprends le code.

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
image: salima.jpg

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Je me présente !
    description: Je m'appelle Salima, je suis la formation DA Android, voici mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/salima/project1.png
    image: salima/projet_1.jpg, screenshotlinkedin/projet_1.jpg;
    link: http://www.linkedin.com/in/salima-rabia
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull req.
    image: salima/projet_2.jpg
    link: https://openclassrooms-student-center.github.io/presentation/students/salima.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: salima/projet_3.jpg
    link: https://www.github.com/salima017
    finished: true
  - title: Projet, mon beau projet !
    description: Création d’un nouveau dossier pour organiser les photos de mes projets.
    # Create a new folder for images of my projetcs, named salima.
    # Images must be light, less than 200ko and be located here: content/images/students/salima
    image: salima/projet_1.jpg, screenshotlinkedin/projet_1.jpg, salima/projet_2.jpg;
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture.
    finished: true
---
