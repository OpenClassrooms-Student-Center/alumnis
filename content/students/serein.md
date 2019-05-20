---

# FILENAME : serein.md
# Example: 
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: serein

# First name or full name
name: Serein
date: 2019-04-26 15:30

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Me reconvertir dans le numérique pour vivre de ma passion pour le digital.

# max 100 characters
short_description: Passionné de sport et de digital, j'aime pratiquer le basketball, le judo et adore voyager.

# don't touch that
template: students

# max 500 characters
description:
    Passionné par le sport et le numérique, je pratique de manière fréquente
    le basket-ball en championnat régional et départemental. Toutefois,
    je suis un adepte de l'e-sport et je fais partie d'une association
    de gamers de la région de Charente.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
# max size: 200ko
image: smeidom.jpg

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Présentez-vous !
    # max 100 characters
    description: Serein, 28 ans, apprenti développeur Python en reconversion.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/images/students/yourrepo/project1.png
    image: serein123/projet1.png
    link: https://www.linkedin.com/in/serein-meidom-747164185/
    # 'true' makes it public. If 'false', then it will not show on the website.
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests.
    image: serein123/projet2.png
    link: https://github.com/smeidomk/alumnis
    finished: false
  - title: Aidez MacGyver à sortir !
    description: Création d’un jeu développé en Python et utilisant PyGame.
    image: serein123/projet3.png
    link: https://github.com/smeidomk/
    finished: false
---