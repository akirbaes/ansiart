#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Charamatrix import Charamatrix
import colorama
colorama.init()

card = Charamatrix().load_data("CARD_FRONT.aas")
coeur = Charamatrix().load_data("petit_coeur.aas")
carreau = Charamatrix().load_data("petit_carreau.aas")
trefle = Charamatrix().load_data("petit_trefle.aas")
pique = Charamatrix().load_data("petit_pique.aas")
couleurs = [coeur,carreau,trefle,pique]

as_coeur = Charamatrix().load_data("coeur.aas")
as_carreau = Charamatrix().load_data("carreau.aas")
as_trefle = Charamatrix().load_data("trefle.aas")
as_pique = Charamatrix().load_data("pique.aas")
as_couleurs = [as_coeur,as_carreau,as_trefle,as_pique]

noms = ("coeur","carreau","trefle","pique")

card_width = 20 #+2 +2
image_width = 16
card_height = 14 #+1 +1
image_height = 12

#knots="♥♦♣♠"
knots=b'\x03\x04\x05\x06'.decode("utf-8") #this works!!!
fgcolors=[Charamatrix.RED,Charamatrix.RED,Charamatrix.BLACK,Charamatrix.BLACK]
bgcolor=Charamatrix.WHITE
red=Charamatrix.RED
black=Charamatrix.BLACK
###2

w=20
w1=w//3
w2=w//2-1
w3=w*2//3-1

h=14

u=3
m=6
d=9

ulx=2
uly=1

drx=w-4
dry=h-2
"""
seven = card.copy()
seven.write(ulx,uly,"7"+knots[1],bgcolor,red)
seven.paste(w1,u,carreau)
seven.paste(w3,u,carreau)

seven.paste(w1-2,m,carreau)
seven.paste(w2,m,carreau)
seven.paste(w3+2,m,carreau)

seven.paste(w1,d,carreau)
seven.paste(w3,d,carreau)

seven.write(drx,dry,"7"+knots[1],bgcolor,red)
seven.save_data("carreau_7.aas")
print(seven.export_ansi())"""

screen = Charamatrix(80,10*h)
for c in range(4):
	one = card.copy()
	two = card.copy()
	three = card.copy()
	four = card.copy()
	five = card.copy()
	six = card.copy()
	seven = card.copy()
	eight = card.copy()
	nine = card.copy()
	ten = card.copy()
	river = [one,two,three,four,five,six,seven,eight,nine,ten]
	for i,ca in enumerate(river):
		ca.write(ulx,uly,str(i+1)+knots[c],bgcolor,fgcolors[c])
		ca.write(drx-(i==9),dry,str(i+1)+knots[c],bgcolor,fgcolors[c])
	
	one.paste(2,4,as_couleurs[c])
	two.paste(w2,u,couleurs[c])
	two.paste(w2,d,couleurs[c])

	three.paste(w2,u,couleurs[c])
	three.paste(w2,m,couleurs[c])
	three.paste(w2,d,couleurs[c])

	four.paste(w1,u,couleurs[c])
	four.paste(w3,u,couleurs[c])
	four.paste(w1,d,couleurs[c])
	four.paste(w3,d,couleurs[c])

	five.paste(w2,m,couleurs[c])
	five.paste(w1,u,couleurs[c])
	five.paste(w3,u,couleurs[c])
	five.paste(w1,d,couleurs[c])
	five.paste(w3,d,couleurs[c])

	six.paste(w1,m,couleurs[c])
	six.paste(w3,m,couleurs[c])
	six.paste(w1,u,couleurs[c])
	six.paste(w3,u,couleurs[c])
	six.paste(w1,d,couleurs[c])
	six.paste(w3,d,couleurs[c])

	seven.paste(w1,u,couleurs[c])
	seven.paste(w3,u,couleurs[c])

	seven.paste(w1-2,m,couleurs[c])
	seven.paste(w2,m,couleurs[c])
	seven.paste(w3+2,m,couleurs[c])

	seven.paste(w1,d,couleurs[c])
	seven.paste(w3,d,couleurs[c])


	eight.paste(w1,u,couleurs[c])
	eight.paste(w3,u,couleurs[c])

	eight.paste(w2,u+1,couleurs[c])

	eight.paste(w1,m,couleurs[c])
	eight.paste(w3,m,couleurs[c])

	eight.paste(w2,m+1,couleurs[c])

	eight.paste(w1,d,couleurs[c])
	eight.paste(w3,d,couleurs[c])
	
	
	nine.paste(w1-2,u,couleurs[c])
	nine.paste(w2,u,couleurs[c])
	nine.paste(w3+2,u,couleurs[c])
	nine.paste(w1-2,m,couleurs[c])
	nine.paste(w2,m,couleurs[c])
	nine.paste(w3+2,m,couleurs[c])
	nine.paste(w1-2,d,couleurs[c])
	nine.paste(w2,d,couleurs[c])
	nine.paste(w3+2,d,couleurs[c])


	ten.paste(w1,u-1,couleurs[c])
	ten.paste(w3,u-1,couleurs[c])

	ten.paste(w2,u,couleurs[c])

	ten.paste(w1,u+1,couleurs[c])
	ten.paste(w3,u+1,couleurs[c])

	ten.paste(w1,m+1,couleurs[c])
	ten.paste(w3,m+1,couleurs[c])

	ten.paste(w2,d-1,couleurs[c])

	ten.paste(w1,d,couleurs[c])
	ten.paste(w3,d,couleurs[c])

	for i in range(len(river)):
		screen.paste((i+10*c)%4*w,(i+10*c)//4*h,river[i])
		river[i].save_data(".export_"+noms[c]+"_"+str(i+1)+".aas")
toprint=screen.export_ansi()
print(toprint)
#.encode("utf-8") or sys.getdefaultencoding()) will turn it into code (with slashes) ---> called on "string" and internal stuff
#.decode("utf-8") will turn it into decyferable thing (into string), from an encoded source
#somehow the export was not using the right representation of triangles... To check. Why  works but not ▲?
