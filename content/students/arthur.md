---

# FILENAME : Arthur
# Example: 
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: arthur

# First name or full name
name: Arthur
date: 2017-11-09 17:15

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Apprendre le métier de l'informatique et surfer sur la vague des nouvelles technologies !
short_description: Amateur de Physique, de jeux-vidéos et de défis sportifs.

# don't touch that
template: students
description:
    J'ai toujours été intéressé par les nouvelles technologies et 
    particulièrement la programmation informatique. J'adore voyager,
    faire du sport et bien sûr geeker.


# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: arthur.png

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentation
    description: Arthur, 22 ans, apprenti développeur Python
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: Arthur/projet1.png
    link: https://www.linkedin.com/in/arthur-di-benedetto-7aa91412a/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: Arthur/projet2.png
    link: https://github.com/MrDiben
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: Arthur/projet3.jpg
    link: https://github.com/MrDiben
    finished: false

---
