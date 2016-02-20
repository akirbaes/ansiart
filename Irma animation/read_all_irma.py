ESC= '\033['
import colorama
from Charamatrix import Charamatrix
colorama.init()

def SETXY(x,y):
	return ESC+str(y)+';'+str(x)+'H'


screen = Charamatrix(80,24)
animation=list()

for index in range(4):
	name="irma_anim"+str(index)
	card=Charamatrix()
	card.load_data(name+".aas")
	animation.append(card)

import sys
from time import sleep
while(True):
	for index,card in enumerate(animation):
		#screen.fill(" ",0,0) #use? used for melon
		#screen.paste(0,0,card)
		sys.stdout.write(SETXY(0,0)+card.export_ansi())
		sys.stdout.flush()
		sleep(0.07)
