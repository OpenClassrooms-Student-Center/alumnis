---

# FILENAME :use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: camillemaury1

# First name or full name
name: Camille Maury
date: 2017-02-12 15:12

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Python, Java, puis conquérir le monde. 
short_description: 32 ans à Montpellier, Parapentiste et fan d'e-sport

# don't touch that
template: students
description:
    Le dev m'a toujours attiré, et j'envisage de coupler la gestion de projet
    au métier de développeur pour élargir mes possibilités ! 
    Ayant néanmoins un certain amour pour les lettres, j'envisage de laisser
    les deux dernières phrases du Lorem Ipsum. 
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: camillemaury1.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même (voir précédemment) et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: camillemaury1/projet_1.jpg
    link: https://www.linkedin.com/in/camille-maury-7a460714b/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: camillemaury1/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/camillemaury1.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---
