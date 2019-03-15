---

# FILENAME : https://openclassrooms.com/fr/membres/alexandre-cambefort
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: kevin75

# First name or full name
name: Kevin
date: 2018-11-21 10:00

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Pouvoir choisir un poste et en changer facilement si le besoin s'en fait sentir. 
short_description: J'aime le fromage, les comics ainsi que les gadgets et services technologiques.

# don't touch that
template: students
description:
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor 
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
    exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
    fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
    sunt in culpa qui officia deserunt mollit anim id est laborum. 

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: kevin75.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Je suis un parisien de bientôt 40 ans travaillant dans l'informatique depuis 2014, j'apprends à coder pour renforcer mon profil et diversifier mes compétences.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: kevin75/project_1.png
    link: https://www.linkedin.com/in/kevinlebihan/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: kevin75/project_2.png
    link: https://github.com/Kariboupseudo/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: kevin75/projet_3.png
    link: https://github.com/Kariboupseudo/MacGyver
    finished: true
---