# -*- coding: utf-8 -*-
#!/usr/bin/python2
#DOESN'T WORK IN PYTHON3 BECAUSE OF MODULE IMAGE and hasn't figured out how to output in a file in UTF-8 in python 2
import os
from PIL import Image
import codecs

def isPNG(fil):
	return os.path.isfile(fil) and fil.split(".")[-1] == "png"

def comparaison(case, case2):
    ans=0
    for i in range(len(case)):
        for j in range(len(case[0])):
            ans+=case[i][j]==case2[i][j]
    return ans

def plus_ressemblant(case,base):
    """Recoit une matrice case et une liste de matrices base,
renvoie l'ID de la case la plus ressemblante"""
    meilleur=0
    meilleurID=-1
    for i in range(len(base)):
        temp=comparaison(case,base[i])
        if(temp>meilleur):
            meilleurID=i
            meilleur=temp
    return meilleurID
    

baseImage=Image.open("base.png")
width=8
height=13
num=baseImage.size[0] // width #number of images
base=list([list() for i in range(num)])

for i in range(num):
    for y in range(height):
        line=[]
        for x in range(width):
            line+=[baseImage.getpixel((x+width*i,y))]
        base[i].append(line)

imageName=raw_input("Enter file name ([enter]=default)")
if(imageName==""):
	imageName="monstre.png"
picture=Image.open(imageName)

numW,numH=picture.size
numW,numH=numW/width,numH/height


def show_img(case):
    for line in case:
        for elem in line:
            if(elem==(0,0,0)):
                print "X",
            else:
                print " ",
        print "",

"""
for case in base:
    show_img(case)"""

result=[]
for j in range(numH):
    ligne=[]
    for i in range(numW):
        case=[]
        for y in range(height):
            line=[]
            for x in range(width):
                 xx=x+i*width
                 yy=y+j*height
                 line+=[picture.getpixel((xx,yy))]
            case+=[line]
        ligne+=[case]
    result+=[ligne]


final=[]
for ligne in result:
    line=[]
    for case in ligne:
        line+=[plus_ressemblant(case,base)]
    final+=[line]
print (final)

chars=u" ▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐▕░▒▓▔▖▗▘▙▚▛▜▝▞▟■□◢◣◤◥▪▫▬▭▮▯▰▱▲△▴▵▶▷▸►▼◀▾◂◄◆◨◩◪●◼◾◺"


def afficher(matrice):
	ans=""
	for line in matrice:
		for elem in line:
			ans+=chars[elem]
		ans+="\n"
	return ans

ans=afficher(final)
outfile=codecs.open(imageName+".output.txt","w",encoding="utf-8")
outfile.write(ans)
print(ans)
