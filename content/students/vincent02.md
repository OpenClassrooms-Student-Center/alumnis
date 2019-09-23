---

# FILENAME : vincent02.
# Example: https://okenclassrooms.com/membres/yoannroche
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: vincent02

# First name or full name
name: Vincent
date: 2019-05-15 10:01

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Apprendre de nouelles choses sur Python.
short_description:  Dessine beaucoup en voyangeant.

# don't touch that
template: students
description:
    J'apprends à dessiner et à coder sur mon temps libre.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: vincent02.png

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: vincent02/projet_1.png
    link: https://www.linkedin.com/in/vincent-cottéreau-2a1391b5/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: vincent02/projet_2.png
    link: https://github.com/LyKouNeT/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: vincent02/projet_3.png
    link: https://www.github.com
    finished: false
---
