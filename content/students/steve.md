---
# FILENAME : please use your OpenClassrooms's name, available in your url.# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: steve

# First name or full name
name: Steve
date: 2019-03-17 17:05
# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Réussir ma reconversion professionnelle.
short_description: J'aime le krav maga, le chocolat et recevoir mes amis.
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
image: content/images/students/steve.jpg
# Change this to True when you do you pull request.
public: true
# You need to keep the exact same structure for each new project.
projects:
  - title: Projet 1 – Présentez-vous !
    description: Ce projet permet de gagner en visibilité en mettant à jour notre notre CV et notre profil Linkedin.
    # Create a new repository for your images. Name it the same as your nickn ame and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: project1.png
    link: https://www.linkedin.com/in/steve-leroy-61161b68
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté OpenClassrooms !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git/Github et des pull requests. 
    image: project2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/steve.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: Steve/projet_3.png
    link: https://www.github.com
    finished: false
---
