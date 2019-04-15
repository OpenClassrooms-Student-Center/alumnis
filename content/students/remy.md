---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: remy

# First name or full name
name: Remy
date: 2019-04-14 15:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Acquérir des nouvelles compétences et expériences 
short_description: J'aime apprendre, lire, l'escalade ...

# don't touch that
template: students
description:
    Je m'appelle Rémy et je commence le parcours de forma-
	-tion Développement d'application Android. Je viens   
    du secteur de la culture et si vous voulez en savoir  
    plus sur moi, j'ai un site :) entrevousetmoi.weebly.com
   
# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: remy.jpg

# Change this to True when you do you pull request.
public: True
# You need to keep the exact same structure for each new project.
projects:
  - title: Presentation
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: remy/project1.png
    link:  https://www.linkedin.com/in/rémy-pouzet-69089887/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: ratus/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/ratus.html
    finished: false
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---