# FILENAME : https://openclassrooms.com/fr/membres/stoppini-alexandre
# Example : httpss://openclassrooms.com/fr/membres/stoppini-alexandre
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: Alexandre06

# First name or full name
name: Alexandre
date: 2019-07-28 10:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Développer de nouvelles compétences afin de me réorienter et de m'épanouir.
short_description: Grand passionné des sciences et de la compréhension de notre monde.

# don't touch that
template: students
description:
    Après presque trois ans à faire des petits boulots et à me chercher, je me décide enfin à
	chercher une formation qui pourrait réellement me correspondre. J'ai toujours été attiré
	par l'informatique et la programmation de manière générale. Durant l'année de terminale,
	j'ai en effet suivi une spécialité de développement Java.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: alexandre06.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: alexandre06/projet_1.png
    link: https://www.linkedin.com/in/alexandre-stoppini-3a59ba103/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: alexandre06/projet_2.png
    link: https://github.com/alexandre-stoppini/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---