---

# FILENAME : 
# Example: 
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: Badr

# First name or full name
name: Badr Touchna
date: 2017-09-04 02:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Diplôme developpeur d'application Java.

# don't touch that
template: students
description: je m'appelle Badr j'ai 25 ans et je suis passioné d'informatique.
    

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: Badr.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: projet_1.png ; projet-2.png
    link: https://www.linkedin.com/in/badr-touchna-09552a14a/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: projet-2.png
    link: https://github.com/User0904/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---
