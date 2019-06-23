---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: jose

# First name or full name
name: Jose
date: 2019-06-25 16:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Ajouter une nouvelle corde à mon arc.
short_description: J'aime le tennis, Visual Studio et la lecture.

# don't touch that
template: students
description:
    J'aime être au calme ... pour lire un bon thriller par exemple.
    Mais j'aime aussi passer du temps avec mes amis et mes collègues,
    ne serait-ce que pour boire un coup, et partager un bon moment 
    en se remémorrant des souvenirs cultes. J'aime dormir sous une tente 
    en camping et ne pas avoir d'heure pour se lever quitte à ne pas se lever
    du tout. J'adore aussi faire des tartes et les manger aussi bien-sûr. 

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: jose.jpg

# Change this to True when you do your pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: jose/projet_1.png
    link: https://www.linkedin.com/in/jose-garnil
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: jose/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/jose.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---