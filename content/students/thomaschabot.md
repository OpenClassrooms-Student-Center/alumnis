---

# FILENAME : thomaschabot
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: ThomasC

# First name or full name
name: Thomas
date: 2017-10-09 11:00

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Obtenir le titre de Développeur d'applications JAVA
short_description: Je souhaite obtenir le titre de Développeur d'applications JAVA afin d'intégrer une entreprise par la suite pour réaliser une formation en alternance sur deux ans.

# don't touch that
template: students
description:
    Après un cursus commercial, j'ai pris la décision de me réorienter afin de travailler dans un milieu qui me correspond.
    Suite à deux années de formation, je souhaite poursuivre en me spécialisant dans le développement d'applications via le langage JAVA. Egalement intéressé par Android, je travaille en parallèle avec deux amis sur une application mobile.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: thomaschabot.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: thomaschabot/projet_1.jpg
    #link: http://www.ricochet-jeunes.org/auteurs/recherche/10146-olivier-vogel
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: thomaschabot/projet_2.jpg
    link: https://openclassrooms-student-center.github.io/presentation/students/thomaschabot.html
    finished: true
---