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

c_white=(255,255,255)
c_ltgray=(192,192,192)
c_gray=(128,128,128)
c_dkgray=(64,64,64)
c_black=(0,0,0)

COLORS = (c_white,c_ltgray,c_gray,c_dkgray,c_black)

def nearest(rgb,clist):
	MIN = 256*3
	ANSWER = None
	R,G,B = rgb
	for color in clist:
		r,g,b = color
		CURRENT = abs(R-r) + abs(G-g) + abs(B-b)
		if(CURRENT==0):
			return color
		if(CURRENT<MIN):
			ANSWER = color
			MIN = CURRENT
	return ANSWER

def difference(RGB,rgb):
	R,G,B = RGB
	r,g,b = rgb
	return abs(R-r) + abs(G-g) + abs(B-b)

def empty():
	return "─"

def half_pixels(color1,color2):
	#choisit quelle moitié selon si l'alpha de la couleur 1 ou 2 est zéro
	if(color1==white):
		return "▄"
	return "▀"
result=""

def colorchar(color1):
	if(color1==white):
		char=empty()
	elif(color1==ltgray):
		char = "░"
	elif(color1==gray):
		char = "▒"
	elif(color1==dkgray):
		char = "▓"
	elif(color1==black):
		char = "█"
	else:
		char = "#"
	return char

for j in range(height//2):
	for i in range(width):
		color1 = surf.get_at((i,j*2))
		color2 = surf.get_at((i,j*2+1))
		
		c1 = color1.r, color1.g, color1.b
		c2 = color2.r, color2.g, color2.b
		
		if(color1.a==color2.a==0): #vide
			char = empty()
			
			
		else:
			color1 = nearest(c1,COLORS)
			color2 = nearest(c2,COLORS)
			if(color1==color2): #plein
				char = colorchar(color1)
			else:
				if(color2==white or color1==white): #demi-pixel (demi vide)
					char = half_pixels(color1,color2)
				else: #demi pixel mais de deux couleurs : impossible donc plein par défaut
					if(color1==ltgray):
						color1 = white
					if(color1==dkgray):
						color1 = black
					if(color2==ltgray):
						color2 = white
					if(color2==dkgray):
						color2 = black
						
					if(color1 == color2):
						char = colorchar(color1)
					elif(color1 == gray and color2 == white)\
					or(color2 == gray and color1 == white):
						char = colorchar(ltgray)
					elif(color1 == gray and color2 == black)\
					or(color2 == gray and color1 == black):
						char = colorchar(dkgray)
					else:
						char = half_pixels(color1,color2)
		result+=char
	result+= """
""" #nouvelle ligne

file = open(file+".nbw.txt","w",encoding='utf-8')
file.write(result)
file.close()

#la couleur de fond est sans balises ; entourer le tout par la balise color de votre choix

pygame.quit()
