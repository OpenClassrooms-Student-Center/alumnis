---

title: paul-emmanueldossantosfacao
name: Paul-Emmanuel DOS SANTOS FACAO
date: 2019-06-17 18:18
objective: Devenir expert Java full stack et utiliser mes compétences transverses.
short_description: Il y a les défis que j'ai relevés et ceux que je n'ai pas attaqués.

# don't touch that
template: students
description:
    Je m'appelle Paul-Emmanuel et à 50 ans je reviens à l'informatique après 20 ans de disgression.

    Être  développeur d'application Java est juste la première étape pour être 
    un futur expert Java Full Stack. 

    Je suis très sportif et passionné de la culture Coréenne.

image: paul-emmanueldossantosfacao.jpg

# Change this to True when you do you pull request.
public: true

projects:
  - title: Présentez-vous !
    description: Une présentation de moi-même et un lien vers mon LinkedIn.
    image: paul-emmanueldossantosfacao/projet_01_cv_paulemmanuel.png
    link: https://www.linkedin.com/in/pedsf/
    finished: true
  - title: Intégrez la communauté !
    description: Modifier un projet Open Source pour comprendre le fonctionnement de Git, de Github et des pull requests. 
    image: paul-emmanueldossantosfacao/projet_02_git.png
    link: https://github.com/pedsf1968/alumnis.git
    finished: true
  - title: Mettez votre logique à l'épreuve
    description: Implémenter Java un jeu en ligne de commande de type MasterMind ou l'on utilise une IA en fonction du mode d'exécution. En mode challenger on doit trouver le code de l'ordinateur en un nombre minimum de coup. En en mode défenseur c'est l'inverse, l'IA essaye de trouver notre code. En mode duel c'est l'un contre l'autre et le premier qui trouve a gagner. J'ai complèté le jeu en ajoutant le choix de la vrai règle du MasterMind. La possibilité au joueur de spécifier la longueur du code à déterminer est donnée ainsi qu'un mode IA contre IA.
  	image:
  	link: https://github.com/pedsf1968/mastermind.git
  	finished: true
  - title: Analysez les besoins de votre client pour son groupe de pizzerias
    description: Etablir les spécifications fonctionnelles d'un système de gestion d'un groupe de pizzérias. Lister les différents acteurs et leurs intéractions avec le système. Décrire les fonctionalités et décrire le cycle de vie d'une commande. Présenter une solution technique.
    image: paul-emmanueldossantosfacao/projet_04_diagramme_cas_utilisation_package_commandes.png
    link: https://github.com/pedsf1968/OC-P4.git
    finished: true
  - title: Concevez la solution technique d’un système de gestion de pizzeria
    description: Etablir le document des spécifications techniques d'un système de gestion d'un groupe de pizzérias. Décrirele les différents composants du système internes et externes utilisés par le système et leurs intéreactions. Etablir le Modèle Physique de Données avec un script SQL contenant un dump de la base avec un jeu de données. Décrire le déploiement de l'application.
    image: paul-emmanueldossantosfacao/projet_05_mdp.png
    link: https://github.com/pedsf1968/OC-P5.git
    finished: true
  - title: Créez un site communautaire autour de l’escalade
    description: Implémenter un site web pour une communauté de grimpeur. Utiliser le language propre à l'escalade. Un utilisateur doit pouvoir s'inscrire pour réserver ou mettre en ligne des Topologies. Le découpage du Modèle Physique de Données a été effectuer pour permettre à de décrire les Topologies de différents type. Un Topo peut avoir des Secteurs et des Voies. Un Secteur contient une ou plusieurs Voies. Pour chaque Topo, Secteur et Voies on peut ajouter une photo, une carte, définir les coordonnées GPS, ajouter des commentaires et différentes informations. Une voie est découpée en une ou plusieurs Longueurs et chaque Longueur comporte des Spits. Les membres peuvent résever et créer des Topos et ajouter leurs commentaires. L'administrateur peut annoter des Topos et supprimer des commentaires. 
    L'application a été Dockerisée et déployée sur une instance EC2 de AWS en utilisant une image Postgres:alpine pour la base de données. Une API restful a été implémenté en plus pour communiquer directement avec la base de données.
    image:
    link: https://github.com/pedsf1968/escalade-web.git
    finished: true
  - title: Développez le nouveau système d’information de la bibliothèque d’une grande ville
    description: Implémenter la partie backend d'une application de gestion de bibliothèque ainsi que sa partie frontend pour les utilisateurs et un batch pour effectuer les relances par internet. Le système peut gérer plusieurs types de média (livre, musiques, films et jeux). Un utilisateur peut s'inscrire et rechercher un média suivant différents critères pour pouvoir le réserver. La période d'emprunt, le nombre de média empruntable et le nombre de reconduction et paramètrable dans un fichier de propriétés. L'application est découpées en plusieurs microservices pour permettre une indépendance des différentes parties et une scalabilité. Chaque microservice est déployé dans un contenneur Docker. Un serveur de configuration permet de centraliser les configurations de tous les microservices dans un dépôt sur GitHub. Un serveur ZUUL est utilisé comme gateway dans le système. On utilise un serveur Eureka comme service discovery et en utilisant OpenFeign et Ribbon on fait du load balancing. Les requêtes entre les microservices sont effectuées en utilisant le spring.application.name et ZUUL envoie à la bonne addresse avec le bon port. Le microservice media-api permet de centraliser les images et renvoie le code byte sur simple requête GET. Les images sont classées dans dezs répertoires suivant le type de média et suivant l'identifiant média. Le microservice user-api est un controlleur restful pour gérer les utilisateurs et l'authentification. le microservice library-api est le controlleur restful pour gérer la partie métier. C'est avec lui que l'on fait les commandes CRUD sur les médias et les emprunts. Web-api est la partie frontend pour les utilisateurs qui utilise en plus Thymeleaf et Bootstrap. Un batch a été ajouter qui interroge une fois par jour le microservice library-api pour avoir la liste des retard. Il envoie ensuite les messages pour les utilisateurs sous forme de Json à un serveur Kafka (CloudKarafka). Un controleur restful mail-api interroge le serveur kafka pour récupérer chaque message et l'envoyer sous forme de mail aux utilisateurs (à Mailtrap). L'utilisation d'un serveur kafka permet d'éviter de saturer le serveur mail. 
    Les microservices sont dockerisés et déployé avec un fichier docker-compose.yml.
    image:
    link: https://github.com/pedsf1968/library.git
    finished: true
---