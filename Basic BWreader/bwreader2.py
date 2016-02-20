#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
screen = pygame.display.set_mode((1, 1))

print("What file do you want to load?")
file=input() #l'image doit être à côté, mettez l'extension dedans

surf = pygame.image.load(file).convert_alpha()

width, height = surf.get_size()
white=pygame.Color(255,255,255,255)
ltgray=pygame.Color(192,192,192,255)
gray=pygame.Color(128,128,128,255)
dkgray=pygame.Color(64,64,64,255)
black=pygame.Color(0,0,0,255)

def empty():
	return "─"

def half_pixels(color1,color2):
	#choisit quelle moitié selon si l'alpha de la couleur 1 ou 2 est zéro
	if(color1==white):
		return u"▄"
	return u"▀"
result=""


for j in range(height//2):
	for i in range(width):
		color1 = surf.get_at((i,j*2))
		color2 = surf.get_at((i,j*2+1))
		
		if(color1.a==color2.a==0): #vide
			char = empty()
		elif(color1==color2): #plein
			if(color1==white):
				char=empty()
			elif(color1==ltgray):
				char = u"░"
			elif(color1==gray):
				char = u"▒"
			elif(color1==dkgray):
				char = u"▓"
			elif(color1==black):
				char = u"█"
			else:
				char = "#"
		else:
			if(color2==white or color1==white): #demi-pixel (demi vide)
				char = half_pixels(color1,color2)
			else: #demi pixel mais de deux couleurs : impossible donc plein par défaut
				char = "#"
		result+=char
	result+= """
""" #nouvelle ligne

#print(repr(result))
file = open(file+".bw.txt","w",encoding='utf-8')
file.write(result)
file.close()

#la couleur de fond est sans balises ; entourer le tout par la balise color de votre choix

pygame.quit()
