UNUSED : use with graphicsgale exported images

import colorama
from Charamatrix import Charamatrix
from terminal_reader import transform
colorama.init()

for i in range(124):
	name="melon"+str(i).zfill(4)
	work=transform(name+".png")
	work.save_data(name+".aas")
exit()
