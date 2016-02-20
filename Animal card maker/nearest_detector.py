#!/usr/bin/env python
# -*- coding: utf-8 -*-

BLACK = (0,0,0)
LTBLACK = (128,128,128)
RED = (128,0,0)
LTRED = (255,0,0)
GREEN = (0,128,0)
LTGREEN = (0,255,0)
YELLOW = (128,128,0)
LTYELLOW = (255,255,0)
BLUE = (0,0,128)
LTBLUE = (0,0,255)
MAGENTA = (128,0,128)
LTMAGENTA = (255,0,255)
CYAN = (0,128,128)
LTCYAN = (0,255,255)
WHITE = (192,192,192)
LTWHITE = (224,224,224)

BACKGROUND_COLORS = (BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE)
FOREGROUND_COLORS = (BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE,\
LTBLACK,LTRED,LTGREEN,LTYELLOW,LTBLUE,LTMAGENTA,LTCYAN,LTWHITE)

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
    #R,G,B = R+255,G+255,B+255
    #r,g,b = R+255,G+255,B+255
    return abs(R-r) + abs(G-g) + abs(B-b)

def ismix(RGB):
    MIN = 256*256
    ANSWER = None
    for color in FOREGROUND_COLORS:
        #removing the pure color ratios
        current = difference(RGB,color)
        if(current<MIN):
            ANSWER = color,color,100
            MIN = current

    for i in range(len(BACKGROUND_COLORS)):
        for j in range(i+1,len(FOREGROUND_COLORS),1):
            #i+1 if not checking same color
            C1 = BACKGROUND_COLORS[i]
            C2 = FOREGROUND_COLORS[j]
            #50/50
            newcol = [(C1[a]+C2[a])/2 for a in range(3)]
            current = difference(RGB,newcol)
            if(current<MIN):
                ANSWER = C1,C2,50
                MIN = current
            #25/75
            newcol = [(C1[a]+C2[a]*3)/4 for a in range(3)]
            current = difference(RGB,newcol)
            if(current<MIN):
                ANSWER = C1,C2,25
                MIN = current
            #75/25
            newcol = [(C2[a]+C1[a]*3)/4 for a in range(3)]
            current = difference(RGB,newcol)
            if(current<MIN):
                ANSWER = C1,C2,75
                MIN = current
            if(MIN == 0):
                return ANSWER
    return ANSWER


def decide(color1,color2):
    if color1==color2:
        C1,C2,RATIO = ismix(color1)
        if(RATIO==100):
            if C1 in BACKGROUND_COLORS:
                CHAR = " "
            else:
                CHAR = "█"
                #C1 = BLACK 
                #TODO set it to the corresponding bgcolor
        elif(RATIO==25):
            CHAR = "▓"
        elif(RATIO==50):
            CHAR = "▒"
        elif(RATIO==75):
            CHAR = "░"
    else:
        C1 = nearest(color1,FOREGROUND_COLORS)
        C2 = nearest(color2,FOREGROUND_COLORS)
        if(C1==C2):
            if(C1 in BACKGROUND_COLORS):
                CHAR = " "
            else:
                CHAR = "█"
        else:
            if(not (C1 in BACKGROUND_COLORS) and
                not(C2 in BACKGROUND_COLORS) ):
                c1 = nearest(color1,BACKGROUND_COLORS)
                c2 = nearest(color2,FOREGROUND_COLORS)
                
                if(difference(c1,color1)<difference(c2,color2)):
                    C1 = c1
                else:
                    C2 = c2
            if(C1 in BACKGROUND_COLORS):
                CHAR = "▄"
            else:
                CHAR = "▀"
                C2,C1 = C1,C2
    return CHAR,C1,C2
"""
Si 2 couleur même :
    full, ismix
        ismix ratio:
        100:
            si bg, vide
            si fg, full
        50: ▒
        25: ▓
        75:    ░
Sinon nearest sur les deux couleurs
Cas 2 de FG ;
Chercher si même = ok (full)
Chercher si différent :"""
    
