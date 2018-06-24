# ----

# FILENAME : Boris mbaute ndo.
# Example: https://openclassrooms.com/membres/boris-mbaute-ndo
# must be the name of your file. If file name is boris.md, title is boris.
# lowercase, no blank space, Capital case or special character.
title: Boris

# First name or full name
name: MBAUTE
date: 1991-01-01 17:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Developper mes competences

# max 100 characters
short_description: J'aime les belles lettres, le fromage et les pages écornées. J'apprends à coder pour me faire une nouvelle jeunesse.

# don't touch that
template: students

# max 500 characters
description:
    Je suis actuellement etudiant et je travail à temps partiel. Je fais donc la formation de développeur d'applications python en hors temps de travail. Sachant que j'ai fais deux parcours  dans deux domaines d'etude diffeterent, je suis vraiment motivé à réussir.
# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
# max size: 200ko
image: boris.jpg

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    # max 100 characters
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: boris.png
    link: https://www.linkedin.com/in/boris-mbaute-ndo-279515163/
    # 'true' makes it public. If 'false', then it will not show on the website.
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests.
    image: boris/projet_2.png
    link: https://github.com/MBAUTENDO
    finished: true.