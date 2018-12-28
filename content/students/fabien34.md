---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: fabien34

# First name or full name
name: Fabien Lenoir
date: 2018-12-28 21:15

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Avoir de solides bases en programmation pour pouvoir créer des idées d'applications
short_description: Je suis un passionné de l'image et de la vidéo, j'aime aussi la technologie et je suis curieux  d'apprendre de nouvelles choses. J'aime aussi la menuiserie et la course à pieds.

# don't touch that
template: students
description:
    En quelques mots, j'ai déjà un parcours dans l'audiovisuel surtout sur les aspects techniques (tournage, montage, régie mobile, éclairage, son, etc...). J'évolue aussi aujourd'hui dans des environnements cloud et tous les écosystèmes de déploiements associés. Je souhaite aujourd'hui renforcer ces connaissances avec des compétences de développement pour  pouvoir aller plus loin dans l'automatisation des workflows et surtout pouvoir créer des programmes en fonctions des idées qui peuvent apparaître. 

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: fabienlenoir.jpg

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même au travers de mon profile Linkedin. J'y ai recensé mon parcours de formation ainsi que détaillé mes expérreinces professionelles ainsi que certains projets. Il y a aussi un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: fabien34/projet1.jpg
    link: https://www.linkedin.com/in/fabienlenoir/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Application pur créer des infographies à partir de données de vote aux élections municipales.
    description: Il s'agit d'un petit projet qqui permettait d'accélérer la création d'infographie en récupérant, en temps réel, les résultats es votes aux élections municpales de 2014. repo github https://github.com/flenoir/vote4sud
    image: fabien34/projet2.jpg
    link: http://young-mountain-7673.herokuapp.com/
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Projet pas encore débuté dans le parcours de formation python. Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---