
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: donovan

# First name or full name
name: donovan
date: 2018-11-14 22:11

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Devenir le meilleure programmeur ^^ .
short_description: Passionner par la programmation je souhaite un jour pouvoir créer une maison entièrement autonome

# don't touch that
template: students
description:
    j'ai 22, je suis vosgien, passionner par un peu tout ce qui touche a l'informatique et surtout par la programmation.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: donovan.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: donovan/projet_1.png
    link: https://www.linkedin.com/in/donovan-maurice-391b90174/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: donovan/projet_2.png
    link: https://github.com/tetrew88/alumnis
    finished: true
---
