---

# FILENAME : 
# Example: 
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: franck

# First name or full name
name: Franck DELRUE
date: 2017-09-24 19:54

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Apprendre à programmer en Java et préparer une reconversion.
short_description: J'aime apprendre de nouvelles choses et de les mettre en pratique.

# don't touch that
template: students
description:
    Travaillant à l'étranger, dans le domaine de la logistique. J'aime découvrir et apprendre de nouvelles choses et de rencontrer 
    des personnes intéressant avec qui partager. J'ai besoin de nouvelles compétences pour pouvoir avancer dans mon travail.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: franck06.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Je me présente ci-dessus :)
    description: https://www.linkedin.com/in/nicolassarkozy/?ppe=1
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: franck/projet_1.png
    link: https://www.linkedin.com/in/franck-delrue-663259150/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: franck/projet_2.png
    link: https://github.com/Heidoji/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet3.png
    link: https://github.com/eviancode
    finished: false
---
