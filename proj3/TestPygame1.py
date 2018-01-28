# -*- coding: utf-8 -*-


import random
import pygame
from pygame.locals import *
from labyrinthe import *

pygame.init()

# quelques constantes
taille_case = 50
largeur = 15 # nombre de cases
hauteur = 15 #nombre de cases
height = taille_case * hauteur
width = taille_case * largeur


# on instancie la fenêtre d'affichage, on la nomme et on rajoute une icône
fenetre = pygame.display.set_mode((height,width))
pygame.display.set_caption("Labyrinthe")
icone = pygame.image.load("icone2.jpg")
pygame.display.set_icon(icone)


# On instancie le labyrinthe et on lui ajoute un personnage
laby = Labyrinthe(15,"labytest.txt",[0,0],[0,14],2)
laby._set_character('McGyver')

# On instancie du texte qu'on va afficher par la suite quand l'utilisateur aura trouvé la sortie
font=pygame.font.Font("cubic.ttf", 90)
font2=pygame.font.Font("cubic.ttf", 60)
text = font.render("",1,(255,0,0))
text2 = font2.render( "Recommencer",1,(255,0,0))
text3 = font2.render( "(Press Enter)",1,(255,0,0))
text4 = font.render("",1,(255,0,0))

#Boucle du jeu
perdu = False
game_over = False
while not game_over :
    
    #Limitation de vitesse de la boucle
    #30 frames par secondes pour ne pas 
    #surcharger le processeur
    pygame.time.Clock().tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #essentiel pour que la fenêtre se ferme quand on clique sur la croix dans le coin
            game_over = True
        
        
        #Ici on implémente les mouvements du caractère en fonction des instructions de l'utilisateur    
        if event.type == pygame.KEYDOWN:
            
            if((laby.character.position != laby.end or laby.character.bag < laby.minobject) and perdu == False):
            
            
                if event.key == pygame.K_RIGHT:
                    b = laby.bouge('d')
                
                elif event.key == pygame.K_LEFT:
                    b=laby.bouge('g')
            
                elif event.key == pygame.K_UP:
                    b=laby.bouge('h')
              
                elif event.key == pygame.K_DOWN:
                    b=laby.bouge('b')
                
                
                # si le personnage est sur une case gardien on met perdu à True
                # et donc on ne rentrera plus dans la boucle et le personnage
                # est donc bloqué
                x = laby.character.position[0]
                y = laby.character.position[1]
                if laby.murs[x][y] == 'g':
                    print(" ")
                    perdu = True
                
            
            # Là une condition permettant de restart le jeu quand l'utilisateur clique sur Entrée
            if event.key == pygame.K_RETURN:
                print("on recommence")
                perdu = False
                laby = Labyrinthe(15,"labytest.txt",[0,0],[0,14],3)
                laby._set_character('McGyver')
                
                
    
    
    
    laby.affiche(fenetre) #On affiche le labyrinthe dans la fenêtre
    
    #Ici une condition qui permet d'afficher du texte dans la fenêtre quand la partie est gagnée
    if(laby.character.position == laby.end and laby.character.bag == laby.minobject):
        fenetre.blit(text, (160,250))
        fenetre.blit(text2,(140,465))
        fenetre.blit(text3,(140,558))
        
    x = laby.character.position[0]
    y = laby.character.position[1]
    
    
    if laby.murs[x][y] == 'g' :
        fenetre.blit(text4, (160,250))
        fenetre.blit(text2,(140,465))
        fenetre.blit(text3,(140,558))
    
    pygame.display.flip() #update fenetre
    
    
pygame.quit()
quit()