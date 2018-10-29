---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: robin1

# First name or full name
name: Valentin
date: 2018-10-29 04:12

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Apprendre Python et me faire une place dans le monde du travail en tant que développeur.
short_description: Je m'appelle Valentin, j'aime certaines choses et je n'en n'aime pas d'autres.

# don't touch that
template: students
description:
    Je m'appelle Valentin Robin, j'ai eu 28 ans il y a très peu de temps et j'aime principalement les jeux vidéo, le métal, l'informatique, les chatons et les gateaux. J'ai commencé la formation car j'ai pour une fois envie de décider de mon orientation et pour me prouver que j'en suis capable.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: robin1.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: robin1/projet_1.jpg
    link: https://www.linkedin.com/in/valentin-robin-802296171/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: robin1/projet_2.jpg
    link: https://github.com/elmasta/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: robin1/projet_3.jpg
    link: https://github.com/elmasta/py.labyrinth
    finished: false
---