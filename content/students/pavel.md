---

# FILENAME : please use your OpenClassrooms's name, available in your url.
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: pavel

# First name or full name
name: Pavel
date: 2019-09-05 20:40

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Approfondir mes connaissances et devenir un véritable expert dans le domaine informatique.
short_description: Passionné par la high-tech, j’apprends à coder pour en faire mon métier.

# don't touch that
template: students
description:
    J’aime la musique, le cinéma, les jeux vidéos. L’audiovisuel est mon deuxième passion, après l'informatique, et c’est pour cette raison que je voudrais travailler sur des applications de traitement d’image, de vidéo, de la modélisation 3D, etc.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: pavel.jpg

# Change this to True when you do you pull request.
public: True

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: pavel/projet-1.png
    link: https://www.linkedin.com/in/pavel-rodin-29431a16a/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: pavel/projet-2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/pavel.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: pavel/projet-3.png
    link: https://www.github.com
    finished: false
---