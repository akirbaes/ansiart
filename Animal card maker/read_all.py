contenu = ["CARD_BACK"]
animaux= "vache","tortue","tigre","tardigrade","souris","serpent","rat","poule","poisson","perroquet","panda","ours","lion","lapin","hibou","herisson","hamster","fourmi","escargot","corbeau","cochondinde","cochon","chien","cheval","chauve","chat","araignee","aigle","cactus"
animaux = [".export_animal_"+name for name in animaux]
aliments= "banane","chips","curry","frite","fromage","fruit","glace","hamburger","patate","pates","pizza","poire","pomme","puree","sandwiche","saucisson","steak","tomate"
aliments = [".export_food_"+name for name in aliments]

contenu.extend(animaux)
contenu.extend(aliments)

card_width = 20 #+2 +2
image_width = 16
card_height = 14 #+1 +1
image_height = 12

import colorama
from Charamatrix import Charamatrix
colorama.init()

card = Charamatrix()
screen = Charamatrix(80,(len(contenu)+3)//4*card_height)


for index,name in enumerate(contenu):
	card.load_data(name+".aas")
	screen.paste((index%4)*card_width,(index//4)*card_height,card)
print(screen.export_ansi())
