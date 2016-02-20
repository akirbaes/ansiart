animaux = "vache","tortue","tigre","tardigrade","souris","serpent","rat","poule","poisson","perroquet","panda","ours","lion","lapin","hibou","herisson","hamster","fourmi","escargot","corbeau","cochondinde","cochon","chien","cheval","chauve","chat","araignee","aigle","cactus"
aliments = "banane","chips","curry","frite","fromage","fruit","glace","hamburger","patate","pates","pizza","poire","pomme","puree","sandwiche","saucisson","steak","tomate"

card_width = 20 #+2 +2
image_width = 16
card_height = 14 #+1 +1
image_height = 12

import colorama
from Charamatrix import Charamatrix
from terminal_reader import transform
colorama.init()


card = Charamatrix()
card.load_data("CARD_BACK.aas")
screen = Charamatrix(80,(len(animaux)+3)//4*card_height)
matrixes = []

for index,name in enumerate(animaux):
	work=transform(name+".png")
	#work.save_data(".export_"+name+".aas")
	p2 = card.copy()
	p2.paste(2,1,work)
	decal=image_width/2+len(name)//2-len(name) #centered position
	
	#comment next line to not write names
	p2.write(2+decal,12,name.capitalize(),Charamatrix.WHITE,Charamatrix.BLACK)
	screen.paste((index%4)*card_width,(index//4)*card_height,p2)
	p2.save_data(".export_animal_"+name+".aas")
print(screen.export_ansi())


screen = Charamatrix(80,(len(aliments)+3)//4*card_height)
for index,name in enumerate(aliments):
	work=transform(name+".png")
	#work.save_data(".export_"+name+".aas")
	p2 = card.copy()
	p2.paste(2,1,work)
	decal=image_width/2+len(name)//2-len(name) #centered position
	
	#comment next line to not write names
	p2.write(2+decal,12,name.capitalize(),Charamatrix.WHITE,Charamatrix.BLACK)
	screen.paste((index%4)*card_width,(index//4)*card_height,p2)
	p2.save_data(".export_food_"+name+".aas")


print(screen.export_ansi())

