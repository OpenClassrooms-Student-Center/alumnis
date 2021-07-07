---

# FILENAME : Souhail
# Example:
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: souhail

# First name or full name
name: souhail
date: 2019-08-29 08:30

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Réussir ma reconversion professionnelle dans le développement web !
short_description: Basketteur et gourmands.

# don't touch that
template: students
description:
 J'aime réaliser des projets, ce que je retrouve dans le développement web. J'aime aussi me dépasser dans le sport. 

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: souhail.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentation 
    description: Souhail, 29 ans, développeur Python en formation.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: souhail/projet_1.png
    link: https://www.linkedin.com/in/souhail-souid-81181915b/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: souhail/projet_2.png
    link: https://github.com/souhailsouid
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: souhail/projet_3.png
    link: https://github.com/souhailsouid
    finished: false
---