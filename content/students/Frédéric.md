---

# FILENAME : https://openclassrooms.com/fr/membres/frederic-courbin-1
# Example: https://openclassrooms.com/membres/celinemartinet
# must be the name of your file. If file name is celinemartinet.md, title is celinemartinet.
# lowercase, no blank space, Capital case or special character.
title: Fr�d�ric

# First name or full name
name: Fr�d�ric
date: 2016-10-28 17:20

# One line.
# If you need more space, go to the next line and add 4 spaces on the left, as in 'description'.
objective: Devenir ind�pendant et m'installer � l'�tranger.
short_description: De nature discr�te, plut�t renferm�, ce changement est salvateur.

# don't touch that
template: students
description:
    Amoureux des immenses for�ts ouest-cannadiennes, plus proche de la nature que de l'agitation quotidenne humaine.
	Je suis passionn� de connaissances, d'art antique, de lecture et de musique classique, je pratique l'escalade, 
	la plong�e autonome, le tir et la randonn�e. Et j'aime par dessus tout la sagesse induite dans les textes anciens,
	malheureusement trop peu pr�sente � notre �poque. Apr�s dix ans pass�s dans le commerce, je souhaite me reconvertir 
	pour voguer vers de nouveaux horizons.

# image must be located in content/images/students
# name should be the same as this file. Eg: celinemartinet.png
image: Fr�d�ric.jpg

# Change this to True when you do you pull request.
public: False

# You need to keep the exact same structure for each new project.
projects:
  - title: Pr�sentez-vous !
    description: Une pr�sentation de moi-m�me et un lien vers mon LinkedIn.
    # Create a new repository for your images. Name it the same as your nickname and profile picture.
    # Image must be here: content/students/yourrepo/project1.png
    image: Fr�d�ric/project_1.png
    link: https://www.linkedin.com/in/fr%C3%A9d%C3%A9ric-courbin-b45435179/
    # 'true' makes it fully available.
    # 'false' will add a black layer on the picture. IT WILL BE PUBLIC!
    finished: true
  - title: Int�grez la communaut� !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: ratus/projet_2.png
    link: https://openclassrooms-student-center.github.io/presentation/students/ratus.html
    finished: true
  - title: Aidez MacGyver � sortir !
    description: Cr�ation d�un jeu d�velopp� en Python et utilisant PyGame.
    image: ratus/projet_3.png
    link: https://www.github.com
    finished: false

---