# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: yves

# First name or full name
name: yves
date: 2016-10-28 17:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: valider le parcours développeur python.

# max 100 characters
short_description: yves guillaume étudiant chez openclassrooms.

# don't touch that
template: students

# max 500 characters
description: Bonjour je fais le parcours développeur python, souhaitant acquérir de nouvelles connaissances, et obtenir une certification valorisante sur mon c.v. j'espere travailler par la suite dans le domaine informatique et plus précisement allié au scientifique, j'espère avoir les capacités.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
# max size: 200ko
image: yves.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    # max 100 characters
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: yves/projet_1.png
    link: https://www.linkedin.com/in/yves-guillaume-5b012018a/
    # 'true' makes it public. If 'false', then it will not show on the website.
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests.
    image: ratus/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/ratus.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
