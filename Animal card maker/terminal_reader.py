#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import Charamatrix
import nearest_detector

def transform(filename):
    screen = pygame.display.set_mode((1, 1))
    surf = pygame.image.load(filename).convert_alpha()
    
    width, height = surf.get_size()
    matrix = Charamatrix.Charamatrix(width, height//2)
    
    for j in range(height//2):
        for i in range(width):
            color1 = surf.get_at((i,j*2))
            color2 = surf.get_at((i,j*2+1))
            color1 = color1.r, color1.g, color1.b
            color2 = color2.r, color2.g, color2.b
            
            CHAR, CBG,CFG = nearest_detector.decide(color1, color2)
            matrix.set(i,j,unicode(CHAR,"utf-8"),CBG,CFG)
    return matrix

if(__name__ == "__main__"):
    print("What file do you want to load?")
    filename=str(raw_input()) #l'image doit être à côté, mettez l'extension dedans
    
    matrix=transform(filename)
    print(matrix.export_ansi())
    matrix.save_ansi(filename[:-4]+".txt")
    matrix.save_data(filename[:-4]+".aas")
            
