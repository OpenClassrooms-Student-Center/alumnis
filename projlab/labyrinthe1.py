# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import random

laby = []

#We load the labyrinth from a txt file

with open ("labytest.txt", "r") as f:
    y = 0
    for line in f:
        laby.append([])
        for character in line:
            laby[y].append(character)
        
        laby[y]=laby[y][0:len(laby[y])-1]
        y=y+1

class Character:
  #Class which define the character by its name and its position.  
    """Classe définissant une personne caractérisée par :
    - son nom
    - sa position"""

    
    def __init__(self, nom, position,bag):
        """we use the '__init__() method with many parameters, the class constructor"""
        self.nom = nom
        self.position = position
        self.bag = bag
        
    def __repr__(self):
        return("Je m'apelle {} et je suis à la position {}.".format( \
                self.nom, self.position))

McGyver = Character('McGyver', [0,0],0)


class Labyrinthe:
    #class defined by its parameters
    """Classe définissant un labyrinthe caractérisé par :
    - sa taille
    - ses murs et ses vides
    - son entrée
    - sa sortie
    - une (ou plusieurs ?) personnes dedans
    """
    
    def __init__(self,taille,murs,begin,end,minobject):
        
        self.taille = taille
        
        laby = []
        with open (murs, "r") as f:
            y = 0
            for line in f:
                laby.append([])
                for character in line:
                    laby[y].append(character)
                laby[y]=laby[y][0:len(laby[y])-1]
                y=y+1
            
                
        self.murs = laby
        
        self.character = Character('defautNom',[0,0],0)
        
        self.begin = begin
        
        self.end = end
        
        self.minobject = minobject
        
        L =[] # liste des numéros des cases vides
        
        for i in range(taille):
            for j in range(taille):
                
                case = laby[i][j]
                
                if case == '0':
                    
                    coordCase = [i,j]
                    L.append(coordCase)
        
        for k in range(self.minobject):
            
            [i,j] = random.choice(L)
            L.remove([i,j])
            self.murs[i][j] = 'o'      
            

    def _set_character(self,nom):
        #we call the method for initializing the character
        """Méthode appelée quand on souhaite initialiser le character"""
        bag= 0
        self.character = Character(nom,self.begin,bag)
        
    def __repr__(self):
        
        a=''
        for k in range(len(self.murs)-1):
            a=a+''.join(self.murs[k])+'\n'
        
        a=a+''.join(self.murs[len(self.murs)-1])
        return(a)
    
    def available_position(self,position):
        
        x=position[0] #première élément de la liste
        y=position[1] # deuxième élément
        
        if x<0:
            return False
        else:
            if x>=self.taille:
                return False
            else:
                if y<0:
                    return False
                else:
                    if y>=self.taille:
                        return False
                    else:
                        if self.murs[x][y]=='1':
                            return False
                        else:
                            return True
        
    def play(self):
        
        while(self.character.position != self.end or self.character.bag<self.minobject):
            
            
            
            
            a=''
            for k in range(len(self.murs)-1):
                u=''.join(self.murs[k])+'\n'
                
                if k == self.character.position[0]:
                    u=''
                    for i in range(len(self.murs[k])):
                        if i == self.character.position[1]:
                            u=u+'X'
                        else:
                            u=u+self.murs[k][i]
                    u=u + '\n'
                
                a=a+u

            u = ''.join(self.murs[len(self.murs)-1])
            
            if len(self.murs)-1 == self.character.position[0]:
                    u=''
                    for i in range(len(self.murs[len(self.murs)-1])):
 
                        if i == self.character.position[1]:
                            u=u+'X'
                        else:
                            u=u+self.murs[len(self.murs)-1][i]
            a=a+u
            
            print(a)
            
            print("Vers où veux tu avancer ? (h,d,b,g)")
            
            c = input()
            
            if c=='h':
                new_position = self.character.position + []
                new_position[0] -= 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print("on bouge et la nouvelle position est :")
                else:
                    print("Impossible d'avancer dans cette direction")

            elif c=='d':
                new_position = self.character.position + []
                new_position[1] += 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print("on bouge et la nouvelle position est :")
                else:
                    print("Impossible d'avancer dans cette direction")
                    
            elif c=='b':
                new_position = self.character.position + []
                new_position[0] += 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print("on bouge et la nouvelle position est :")

                else:
                    print("Impossible d'avancer dans cette direction")

            else :
                new_position = self.character.position + []
                new_position[1] -= 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print("on bouge et la nouvelle position est :")

                else:
                    print("Impossible d'avancer dans cette direction")
            
            
            # On verifie si le personnage est sur une case qui contient un objet et on récupère ou non
            #we check if the character is on a square that contains an object. if yes, we collect it
            x=self.character.position[0]
            y=self.character.position[1]
            
            if self.murs[x][y]=='o':
                self.character.bag +=1
                self.murs[x][y] = '0'
            
            
            
        print("Vous êtes sorti ! Bien joué !")
        
    
    def affiche(self,fenetre):
        #Cette fonction affiche le labyrinthe dans la fenetre donnée en argument, on reprend le code précédent de play
        #this function displays the labyrinth in the window
        
        mur = pygame.image.load("murs2.jpg").convert()
        sortie = pygame.image.load("sortie2.jpg").convert()
        entree = pygame.image.load("entree2.jpg").convert()
        vide = pygame.image.load("vide.png").convert()
        perso = pygame.image.load("perso2.jpg").convert()
        obj = pygame.image.load("object.png").convert()
        gardien = pygame.image.load("gardien.png").convert()
        taille_case = 50
        
        n = len(self.murs)
        
        for i in range(n):
            for j in range(n):
                
                #we calculate the squares's position in pixels
                # on calule la position en pixel (x,y) des différentes cases
                if self.murs[i][j] == 'b': 
                    x = j * taille_case
                    y = i * taille_case
                    fenetre.blit(entree,(x,y))
                    
                elif self.murs[i][j] == '1':
                    x = j * taille_case
                    y = i * taille_case
                    fenetre.blit(mur,(x,y))
                    
                elif self.murs[i][j] == '0':
                    x = j * taille_case
                    y = i * taille_case
                    fenetre.blit(vide,(x,y))
                        
                elif self.murs[i][j] == 'g':
                    x = j * taille_case
                    y = i * taille_case
                    fenetre.blit(sortie,(x,y))
                    
                elif self.murs[i][j] == 'o':
                    x = j * taille_case
                    y = i * taille_case
                    fenetre.blit(obj,(x,y))
                    
               
                
                    
        
        y = self.character.position[0] * taille_case
        x = self.character.position[1] * taille_case
        fenetre.blit(perso,(x,y))
    
    #We implement the function which allow us to move the character in the direction we want
    #Ici on implémente la fonction qui permet de faire bouger le personnage en fonction de la direction donnée en argument
    def bouge(self, direction):
        

        if direction=='h':
            new_position = self.character.position + []
            new_position[0] -= 1
            if self.available_position(new_position)==True:
                self.character.position = new_position
            else:
                return(0)

        elif direction=='d':
            new_position = self.character.position + []
            new_position[1] += 1
            if self.available_position(new_position)==True:
                self.character.position = new_position
            else:
                return(0)
                
        elif direction=='b':
            new_position = self.character.position + []
            new_position[0] += 1
            if self.available_position(new_position)==True:
                self.character.position = new_position

            else:
                return(0)

        else :
            new_position = self.character.position + []
            new_position[1] -= 1
            if self.available_position(new_position)==True:
                self.character.position = new_position

            else:
                return(0)
                
         # On verifie si le personnage est sur une case qui contient un objet et on le récupère ou non
          # #we check if the character is on a square that contains an object. if yes, we collect it  
        x=self.character.position[0]
        y=self.character.position[1]
            
        if self.murs[x][y] =='o':
            self.character.bag +=1
            self.murs[x][y] = '0'
        
            
            
laby = Labyrinthe(15,"labytest.txt",[0,0],[0,14],3)
laby._set_character('McGyver')        
          
 