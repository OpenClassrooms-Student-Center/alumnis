---


# FILENAME : clemencerobin
# Example: https://openclassrooms.com/fr/membres/clemencerobin
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: clemence


# First name or full name
name: Clémence
date: 2019-07-19 11:11


# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Devenir développeuse Python via mon parcours en alternance.
short_description: J'aime l'informatique, je suis végétarienne et je pratique la course à pied.

# don't touch that
template: students
description:
    J'ai 28 ans et je vis à Paris. J'ai postulé pour l'alternance en début d'année.
    De là, j'ai suivi un coaching pour trouver une alternance et c'est chose faire !
    Je suis donc la formation de développeur d'applictions Python pour une durée de deux ans.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: clemence.png

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: clemence/projet_1.png
    link: https://www.linkedin.com/in/clémence-robin/

    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true

  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: clemence/projet_2.png
    link: https://github.com/clemenceclaireR/alumnis
    finished: true

  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false

---
