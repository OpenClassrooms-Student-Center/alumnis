---


# FILENAME : colin.md

# Example: https://openclassrooms.com/membres/colinbrehier

# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.

# lowercase, no blank space, Capital case or special character.

title: colin


# First name or full name

name: colin

date: 2018-01-27 16:20


# One line.

# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.

objective: Apprendre à coder pour en faire mon métier.

short_description: Je suis un pur geek. Passionné de sciences, d'informatique et de jeu vidéo.


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

image: colin.jpg


# Change this to True when you do you pull request.

public: True


# You need to keep the exact same structure for each new project.

projects:

  - title: Présentez-vous !

    description: Je m'appelle Colin, j'ai 26 ans. Je viens de commencer la formation python.

    # Create a new repository for your images. Name it the same as your nickname and profile picture.

    # Image must be here: content/students/yourrepo/project1.png

    image: colin/projet1.png

    link: https://www.linkedin.com/in/colin-brehier-181039157/

    # 'true' makes it fully available.

    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!

    finished: true

  - title: Intégrez la communauté !

    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests.

    image: colin/projet2.png

    link: https://github.com/KanardHeure/alumnis

    finished: true


---