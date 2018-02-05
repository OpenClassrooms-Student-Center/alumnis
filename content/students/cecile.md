---

# FILENAME : celinemartinet
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: cecile

# First name or full name
name: Cecile
date: 2018-02-04 11:10

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Reconversion professionelle pour m'éclater dans mon travail.
short_description: Le code... Tombée dedans quand j'étais petite (BASIC / ATARI :-D )

# don't touch that
template: students
description:
    Après avoir travaillé en gestion de projet informatique (côté fonctionnel), j'ai envie de retourner à mes premiers amours - Le code !
    J'ai codé pour la 1ere fois en Basic.... puis j'ai appris les bases du C et C++ à la fac, me suis amusée avec VBA au travail...
    Maintenant j'ai envie de faire du vrai developpement !

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: cecile.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: cecile/projet1.png
    link: https://www.linkedin.com/in/cecile-mariller-52356b3/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: cecile/projet2.png
    link: https://github.com/cec28/alumnis
    finished: true
  - title: Mémorisez votre humeur du jour
    description: Développement d'une application android "MoodTracker".
    image: cecile/projet3.png
    link: https://openclassrooms.com/projects/memorisez-votre-humeur-du-jour
    finished: false
---