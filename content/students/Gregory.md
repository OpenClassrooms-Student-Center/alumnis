---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: gregory

# First name or full name
name: Grégory
date: 2018-01-25 09:40

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Changer de travail et faire un métier qui me passionne !
short_description: Travailleur, j'adore les casses tète et chercher d'où vient un problème. 

# don't touch that
template: students
description:
    Grand fan du web et tout ce qui touche aux nouvelles technologies.
    Je vis dans la région grenobloise, il y a plein d'activité à faire toute l'année. 
    J'aime le ski l'hiver, la randonnée en été et je peux passer aussi des heures derrière 
    un Pc pour apprendre ou cherche un problème de code ou autres.
    J'ai grandi avec l'informatique et j'espère faire de ma passion mon métier.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: gregory.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: gregory/projet_1.png
    link: www.linkedin.com/in/grégory-oltra-426b52157
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: gregory/projet_2.png
    link: https://github.com/Neoscris/alumnis/blob/gregory/content/images/students/gregory/projet_2.png
    image: gregory/pull_request
    link: https://github.com/Neoscris/alumnis/blob/gregory/content/images/students/gregory/pull_request.png
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---