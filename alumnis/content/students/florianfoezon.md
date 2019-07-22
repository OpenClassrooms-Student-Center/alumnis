---

# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: florianfoezon

# First name or full name
name: florianfoezon
date: 2019-06-18 09:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: acquérir de nouvelles compétences.
short_description: J'apprends à coder pour être plus performant dans mon travail actuel, pour être plus autonome, et pour réaliser concrètement les idées que j'ai dans la tête.

# don't touch that
template: students
description:
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: florianfoezon.jpg

# Change this to True when you do you pull request.
public: true

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    description: Bonjour à vous Openclassrooms! Je suis Florian, et j'intègre le parcours "développeur d'application Java".
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: florianfoezon/projet_1.png
    link: https://www.linkedin.com/in/florian-fo%C3%ABzon-88176022/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: florianfoezon/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/florianfoezon.html
    finished: true
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false
---