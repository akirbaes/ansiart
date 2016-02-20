#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 13, 2014

@author: RedError
'''
from time import time
from random import choice
import codecs
DRAWABLE_CHARACTERS = u"""☺☻♥♦♣♠•○◙♂♀♪♫☼►◄↕‼¶§▬↨↑↓→←∟↔▲▼ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⌂ ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿıƒ‗─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬▀▄█░▒▓■   """

class Charamatrix(object):
    '''
    Matrix of characters to be drawn on a terminal
    Size can vary, can be printed in ANSI-code output
    Each cell can have a foreground, background color and a given character
    A character of "" will mean that the cell is transparent (different from an empty space)
    '''
    
    
    C_BLACK = (0,0,0)
    C_LTBLACK = (128,128,128)
    C_RED = (128,0,0)
    C_LTRED = (255,0,0)
    C_GREEN = (0,128,0)
    C_LTGREEN = (0,255,0)
    C_YELLOW = (128,128,0)
    C_LTYELLOW = (255,255,0)
    C_BLUE = (0,0,128)
    C_LTBLUE = (0,0,255)
    C_MAGENTA = (128,0,128)
    C_LTMAGENTA = (255,0,255)
    C_CYAN = (0,128,128)
    C_LTCYAN = (0,255,255)
    C_WHITE = (192,192,192)
    C_LTWHITE = (224,224,224)
    
    C_FOREGROUND_COLORS = (C_BLACK,C_RED,C_GREEN,C_YELLOW,C_BLUE,C_MAGENTA,C_CYAN,C_WHITE,\
                    C_LTBLACK,C_LTRED,C_LTGREEN,C_LTYELLOW,C_LTBLUE,C_LTMAGENTA,C_LTCYAN,C_LTWHITE)
    C_BACKGROUND_COLORS = (C_BLACK,C_RED,C_GREEN,C_YELLOW,C_BLUE,C_MAGENTA,C_CYAN,C_WHITE)
    
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    LTBLACK = 8
    LTRED = 9
    LTGREEN = 10
    LTYELLOW = 11
    LTBLUE = 12
    LTMAGENTA = 13
    LTCYAN = 14
    LTWHITE = 15
    
    BACKGROUND_COLORS = (BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE)
    FOREGROUND_COLORS = (BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE,\
    LTBLACK,LTRED,LTGREEN,LTYELLOW,LTBLUE,LTMAGENTA,LTCYAN,LTWHITE)
    
    def BGCODE(self,color):
        return(str(color+40))
    
    def FGCODE(self,color):
        return str((color%8+30))
    
    def color_number(self,color):
        return Charamatrix.BACKGROUND_COLORS.index(color)
    
    def is_bg(self,color):
        return color in Charamatrix.BACKGROUND_COLORS
    
    def is_fg(self,color):
        return color in Charamatrix.FOREGROUND_COLORS

    def __init__(self, width=1,height=1):
        '''
        Constructor
        '''
        self.matrix = []
        for i in range(width):
            self.matrix.append([])
            for j in range(height):
                self.matrix[-1].append(["",Charamatrix.BLACK,Charamatrix.WHITE])
                i=j*i
        self.dirty = list()
        self.width = width
        self.height = height
        
        
    def set(self,x,y,char=None,bgcolor=None,fgcolor=None):
        if(isinstance(bgcolor,tuple)):
            bgcolor=Charamatrix.C_FOREGROUND_COLORS.index(bgcolor)%8
        if(isinstance(fgcolor,tuple)):
            fgcolor=Charamatrix.C_FOREGROUND_COLORS.index(fgcolor)
            
        if(self.inside(x,y)):
            data = self.get(x,y)
            if(char==bgcolor==fgcolor==None):
                data = "",data[1],data[2] #force transparency, retain color informations
            else:
                data = char or data[0], \
                data[1] if bgcolor==None else bgcolor, \
                data[2] if fgcolor==None else fgcolor
                #Bug avec color=0 qui ne remplace pas la nouvelle couleur
                
            """if(self.get(x,y)!=data):
                self.dirty.append((x,y))
                self.matrix[x][y]=data"""
            self.matrix[x][y]=data
                
    def put(self, *data):
        self.set(*data)
        
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    
    def inside(self,x,y):
        """Are given x y inside matrix"""
        return 0<=x<self.get_width() and 0<=y<self.get_height()
        print(x,y)
    
    
    def select(self,x,y,w,h):
        """Return a new sub-charamatrix"""
        answer = Charamatrix(w,h)
        for i in range(w):
            for j in range(h):
                if(self.inside(x+i,y+j)):
                    answer.set(i,j,*self.get(x+i,y+j))
                else:
                    answer.set(i,j,"",None,None) #outside, None by default (not necessary)
        return answer
    
    def is_transparent(self,data):
        """Check for special values in a chara tuple"""
        return (data[0]=="" or data[0]==None)
    
    def copy(self):
        """Return a full copy"""
        return self.select(0,0,self.get_width(),self.get_height())
    
    def paste(self,x,y,other,w=None,h=None,transparentHoles=True):
        """Paste other's data onto us in position x,y. Transparency holes means see trough."""
        if(w == None):
            w = other.get_width()
        if(h == None):
            h = other.get_height()
            
        for i in range(w):
            i=i%other.get_width()
            for j in range(h):
                j=j%other.get_height()
                data = other.get(i,j)
                if(not transparentHoles or not self.is_transparent(data)):
                    self.set(x+i,y+j, *data)
    
    def draw_rectangle(self,x=0,y=0,w=None,h=None,character=None,bgcolor=None,fgcolor=None):
        """Rectangle"""
        if(w==None):
            w=self.get_width()
        if(h==None):
            h=self.get_height()
        for i in range(w):
            for j in range(h):
                if(self.inside(x+i,y+j)): #unnecessary, tested in set
                    self.set(x+i,y+j,character,bgcolor,fgcolor)

    def fill(self,character=None,bgcolor=None,fgcolor=None):
        self.draw_rectangle(0,0,None,None,character=character,bgcolor=bgcolor,fgcolor=fgcolor)
                    
    def draw_canvas(self,x1,y1,x2,y2,character=None,bgcolor=None,fgcolor=None):
        """Empty rectangle"""
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)
        
        for i in range(x1,x2,1): #haven't tested if inside, ok because in set
            self.put(i,y1, character,bgcolor,fgcolor)
            self.put(i,y2, character,bgcolor,fgcolor)
            
        for j in range(y1,y2,1):
            self.put(x1,j, character,bgcolor,fgcolor)
            self.put(x2,j, character,bgcolor,fgcolor)
            
    def write(self,x,y,string="",bgcolor=None,fgcolor=None):
        """Write several characters at once (string) in given context
        If too long, wraps locally (from the start of the string)"""
        j=0
        for i, character in enumerate(string):
            if(i>=self.get_width()):
                i=0 #wraps horizontally
                j+=1
                if(j>self.height()):
                    j=0 #warps vertically
            self.put(x+i,y+j,character,bgcolor,fgcolor) #put checks the insides
            
    def read(self,x,y,lenght):
        """Reads and return several characters at once (string)"""
        answer=""
        j=0
        for i in range(lenght):
            if(self.inside(x+i,y+j)):
                answer+=self.get(x+i,y+j)
            elif(x+i>=self.get_width()):
                i=0
                j+=1
                if(y+j>=self.get_height()):
                    j=0
                
        return answer
    
    
    
    def get_matrix(self):
        """Getter for the matrix list-list. Do not use outside?"""
        return self.matrix
    
    def get(self,x,y):
        """Get given position's infos (tuple). Otherwise None. Do not use outside?"""
        if(self.inside(x,y)):
            return self.matrix[x][y]
        else:
            return ("",Charamatrix.BLACK,Charamatrix.WHITE)
        
    def line(self,x1,y1,x2,y2,character=None,bgcolor=None,fgcolor=None):
        x1,x2 = sorted(x1,x2)
        y1,y2 = sorted(y1,y2)
        lenght = min(x2-x1,y2-y1)
        for i in range(lenght):
            x = int(x1+(x2-x1)*i/lenght)
            y = int(y1+(y2-y1)*i/lenght)
            self.set(x,y,character,bgcolor,fgcolor)
            
    #TODO rotate
    
    def export_ansi(self,x=0,y=0,width=None,height=None,fill_blancs=False):
        if(width==None):
            width = self.get_width()
        if(height==None):
            height = self.get_height()
                
        text_data=""
                
        for j in range(height):
            for i in range(width):
                if(self.inside(x+i,y+j)):
                    data = self.get(x+i,y+j)
                    if(self.is_transparent(data)):
                        if(fill_blancs):
                            data="\x1b[0m " #reset color and add a space
                        else:
                            data="\x1b[0m\x1b[1C" #reset color and jump one forward
                    else:
                        char,bg,fg = data
                        if fg in Charamatrix.BACKGROUND_COLORS: #dim version
                            data="\x1b[22" #normal : dimmer on win32
                        else:
                            data="\x1b[1" #bold : bright
                        data += ";" + self.FGCODE(fg) + ";" + self.BGCODE(bg) + "m" + char 
                    text_data+=data
            text_data+="\x1b[0m" #reset
            if(j<height-1): #add a newline except for the last line
                text_data+="\n"
        
        return text_data
        
    def export_data(self,x=0,y=0,width=None,height=None,fill_blancs=False):
        if(width==None):
            width = self.get_width()
        if(height==None):
            height = self.get_height()
                 
        text_data = u"" + chr(self.get_width()) + chr(self.get_height())
        
        for j in range(height):
            for i in range(width):
                if(self.inside(x+i,y+j)):
                    data = self.get(x+i,y+j)
                    if(self.is_transparent(data)):
                        data= "07"+chr(173) #soft hyphen is not a draw-ok character
                    else:
                        char,bg,fg = data
                        data=  hex(fg)[-1] + hex(bg)[-1] + char
                        #bg and fg are 0-15 numbers
                    
                else:
                    data= "07"+chr(173) #soft hyphen is not a draw-ok character
                text_data+= data         
        """
        text_data = str(self.get_width()) + " " + str(self.get_height())
        for j in range(height):
            for i in range(width):
                if(self.inside(x+i,y+j)):
                    data = self.get(x+i,y+j)
                    if(self.is_transparent(data)):
                        data= "07"+chr(173) #soft hyphen is not a draw-ok character
                    else:
                        char,bg,fg = data
                        data= hex(bg)[-1] + hex(fg)[-1] + char
                        #bg and fg are 0-15 numbers
                    
                else:
                    data= "07"+chr(173) #soft hyphen is not a draw-ok character
                text_data+= data
        """
        return text_data

    def save_ansi(self,filename=None):
        """Save the ansi representation of the matrix in a file.
        If no name is given, saves in a newfile_[current_epoch_second].txt"""
        if(filename==None):
            filename = "newfile_"+str(int(time()))+".txt"
        textfile = codecs.open(filename,"w","utf-8")
        textfile.write(self.export_ansi())
        textfile.close()
        
    def save_data(self,filename=None):
        """Save the bg fg char representation of the matrix in a file.
        If no name is given, saves in a newdata_[current_epoch_second].aas"""
        if(filename==None):
            filename = "newdata_"+str(int(time()))+".aas"
        textfile = codecs.open(filename,"w","utf-8")
        textfile.write(self.export_data())
        textfile.close()
        
    def load_data(self,filename,vertical=False):
        """Load and create a new charamatrix if not called on one instance
        vertical is for compatibility with old version"""
        if(filename==None):
            raise Exception("No file name given!")
        save=codecs.open(filename,"r","utf-8")
        mydata = list(u""+save.read())
        save.close()
        w,h = ord(mydata.pop(0)), ord(mydata.pop(0))
        #print("Size : ",w,h)
        if(self==None):
            matrix = Charamatrix(w,h)
        else:
            self.__init__(w,h)
            matrix = self
        for i in range(w*h):
            fg,bg,char = mydata.pop(0), mydata.pop(0), mydata.pop(0)
            #print("popped",fg,bg,char)
            fg,bg,char = int(fg,16), int(bg,16), char
            #print("read",fg,bg,char)
            if(ord(char) == 173): #character is ord(173) caret
                char = None
            if(vertical):
                matrix.set(i//h,i%h,char=char,bgcolor=bg,fgcolor=fg)
            else:
                matrix.set(i%w,i//w,char=char,bgcolor=bg,fgcolor=fg)
        return matrix
        
    def default_random(self,width=None,height=None):
        if(width==None):
            width=self.get_width()
        if(height==None):
            height=self.get_height()
        self.__init__(width,height)
        
        for i in range(width):
            for j in range(height):
                self.set(i,j,choice(DRAWABLE_CHARACTERS),choice(Charamatrix.FOREGROUND_COLORS),choice(Charamatrix.BACKGROUND_COLORS))

    def __repr__(self):
        """For printing.
Since forward jumps don't work on Windows command default,
replaces it with default spaces. """		
        return self.export_ansi(fill_blancs=True)
    def __print__(self):
        return self.export_ansi(fill_blancs=True)
    
    def crop(self):
        """NOT OPTIMISED
        crop ON ITSELF the transparent full areas"""
        width,height = self.get_width(),self.get_height()
        
        left=0
        for i in range(width):
            total=False
            for j in range(height):
                if not(self.is_transparent(self.get(i,j))):
                    break
                if(j==height-1):
                    total=True
            if(not total):
                break
            else:
                left+=1
                
        right=0
        for i in range(width):
            total=False
            for j in range(height):
                if not(self.is_transparent(self.get(width-1-i,j))):
                    break
                if(j==height-1):
                    total=True
            if(not total):
                break
            else:
                right+=1
                
        up=0
        for j in range(height):
            total=False
            for i in range(width):
                if not(self.is_transparent(self.get(i,j))):
                    break
                if(i==width-1):
                    total=True
            if(not total):
                break
            else:
                up+=1
        
                        
        down=0
        for j in range(height):
            total=False
            for i in range(width):
                if not(self.is_transparent(self.get(i,height-1-j))):
                    break
                if(i==width-1):
                    total=True
            if(not total):
                break
            else:
                down+=1
                
        temp=self.select(left,up,width-left-right,height-up-down)
        self.__init__(width-left-right,height-up-down)
        self.paste(0,0,temp,transparentHoles=False)
        
def main():
    mat = Charamatrix(80,20)
    #mat.default_random()
    #print(mat.export_ansi())
    #mat.save_ansi()
    mat.load_data("_CARD_BACK.txt",vertical=True)
    card_width = 20 #+2 +2
    image_width = 16
    card_height = 14 #+1 +1
    image_height = 12
    
    card = mat.select(0,0,card_width,card_height) #could use the new function CROP but this is faster
    #card.save_data("CARD_BACK.aas")
    #card.load_data("CARD_BACK.aas")
    #print(mat.export_ansi(fill_blancs=True))
    
    from terminal_reader import transform
    mat2 = transform("vache.png")
    moocard = card.copy()
    moocard.paste(2,1,mat2)
    
    #print(mat.export_ansi(fill_blancs=True))
    
    screen = Charamatrix(80,20)
    screen.paste(0,0,card)
    screen.paste(card_width+1,1,moocard)
    screen.paste(card_width*2 +2,0,card)
    screen.write(20,card_height+1,"You drew the COW card",0,7)
    print(screen.export_ansi(fill_blancs=True))
    
if __name__=="__main__":
    main()
