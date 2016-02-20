#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
screen = pygame.display.set_mode((1, 1))

print("What file do you want to load?")
file=input() #l'image doit être à côté, mettez l'extension dedans

surf = pygame.image.load(file).convert_alpha()

width, height = surf.get_size()


def hc(integer):
	#représentation hex d'un nombre donné, rallongé à 2 chiffres (<256)
	return hex(integer)[2:].zfill(2)

def hexacol(color):
	#string rrggbb d'une couleur donnée
	return hc(color.r)+hc(color.g)+hc(color.b)

	
def start_color(color):
	return "[color=#"+hexacol(color)+"]"

def end_color(color=None):
	return "[/color]"
	
def empty():
	return "─"
	
def full(color=None):
	if(color!=None and color.a==0): #transparent		
		return "─"
	return "█"

def half_pixels(color1,color2):
	#choisit quelle moitié selon si l'alpha de la couleur 1 ou 2 est zéro
	if(color1.a==0):
		return "▄"
	return "▀"
	
def half_color(color1,color2):
	#renvoie la couleur qui n'est pas transparente (alpha!=0)
	if(color1.a==0):
		return color2
	return color1

result=""
TRANSPARENT = pygame.Color(255,255,255,0) #blanc transparent défaut (n'apparaît pas dans le résultat)

previous_color=[TRANSPARENT] #pour un peu optimiser les balises

for j in range(height//2):
	for i in range(width):
		color1 = surf.get_at((i,j*2))
		color2 = surf.get_at((i,j*2+1))
		
		if(color1.a==color2.a==0): #vide
			char = empty()
			charcol = TRANSPARENT
		elif(color1==color2): #plein
			charcol = color1
			char = full()
		else:
			if(color2.a==0 or color1.a==0): #demi-pixel (demi vide)
				char = half_pixels(color1,color2)
				charcol = half_color(color1,color2)
			else: #demi pixel mais de deux couleurs : impossible donc plein par défaut
				char = full(color1)
				charcol = color1
				
		pc = previous_color[-1]
		if(charcol == pc or pc.a==charcol.a==0):  #pas de changement de couleur
			result+=char
		else:
			if(charcol in previous_color): #fermer des balises ; y'a moyen de faire mieux en optimisation je pense???
				while(charcol!=previous_color[-1]):
					result+=end_color()
					previous_color.pop()
			else:
				previous_color.append(charcol) #ouvrir une nouvelle balise
				result+= start_color(charcol)
			result+=char
	result+= """
""" #nouvelle ligne

for i in range(len( previous_color)-1):
	result += end_color() #fermer les balises restantes

file = open(file+".reader.txt","w",encoding='utf-8')
file.write(result)
file.close()

#la couleur de fond est sans balises ; entourer le tout par la balise color de votre choix

pygame.quit()