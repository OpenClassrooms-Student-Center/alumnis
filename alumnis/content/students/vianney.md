---

# FILENAME : Vianney.diris
# Example: https://openclassrooms.com/membres/vianney-diris
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: vianney

# First name or full name
name: Vianney
date: 2017-07-03 17:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Trouver un emploi en tant que développeur d'application
short_description: Je suis actuellement en reconversion dans le domaine du développement.

# don't touch that
template: students
description:
   Je m'appelle Vianney, je suis né à Bordeaux et je vis à Douai. 
   Je suis le parcours développeur d'application java dans le cadre de ma reconversion.
   Cette reconversion est pour moi un défi que je dois relever.
   J'espère réussir tous les projets et valider mon parcours.


# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: vianney.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: vianney/projet_1.png
    link: https://www.linkedin.com/in/vianney-diris-12924868/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: vianney/projet_2.png
    link: https://github.com/VianneyDiris/alumnis
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---
