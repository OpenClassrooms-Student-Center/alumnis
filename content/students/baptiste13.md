---


# FILENAME : mr13at

# Example: https://openclassrooms.com/membres/celinemartinet

# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.

# lowercase, no blank space, Capital case or special character.

title: 13aptiste


# First name or full name

name: 13aptiste

date: 2018-02-20 11:11


# One line.

# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.

objective: Faire de l'informatique un métier, une carrière, voir toute une philosophie de vie.

short_description: Anciennement employé de Casino, je n'y étais pas par hasard : je suis passionné de Poker.


# don't touch that

template: students

description:

    I've often seen these people, these squares at the table, 

    short stack and long odds against them. All their outs gone. 

    One last card in the deck that can help them. 

    I used to wonder how they could let themselves get into such bad shape, 

    and how the hell they thought they could turn it around. 

    

    Mike McDermott - The Rounders (1998)


# image must be located in content/images/students

# name should be the same as this file. Eg: celinemartinet.png

image: 13aptiste.jpg


# Change this to True when you do you pull request.

public: False


# You need to keep the exact same structure for each new project.

projects:

  - title: Présentez-vous !

    description: Une présentation de moi-même et un lien vers mon LinkedIn.

    # Create a new repository for your images. Name it the same as your nickname and profile picture.

    # Image must be here: content/students/yourrepo/project1.png

    image: 13aptiste/projet_1.png

    link: http://www.linkedin.com/in/carrasco-baptiste

    # 'true' makes it fully available.

    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!

    finished: true

  - title: Intégrez la communauté !

    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 

    image: 13aptiste/projet_2.png

    link: https://github.com/cenotapHe/alumnis

    finished: true

---