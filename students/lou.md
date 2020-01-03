---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: lou

# First name or full name
name: Lou
date: 2019-10-08 10:30

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Réussir ma reconversion professionnelle
short_description: Polyvalente

# don't touch that
template: students
description:
    Je suis Lou, mon objectif principal est de réussir ma reconversion professionnelle et d'obtenir mon diplôme.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: lou.png

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: lou/project_1.png
    link: https://www.linkedin.com/in/lou-fievez/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: lou/project_2.png
    link: https://github.com/justcallmelou
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---