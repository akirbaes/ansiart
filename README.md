# ansiart
Collection of ansi-color ascii-art tools and creations
(using Pygame and Colorama!)

### terminal_reader.py
terminal-reader asks for a file and transform it into
a .txt and a .aas (ansi art save)  
Can also be called by another python file

### nearest_detector.py
nearest_detector is the one doing the transformation  
it calls Pygame  
it is called in terminal_reader for example  
It transforms an image with colored ▄▀█▓▒░ but it has problems with shades (I should do some research about merging and comparing two colors).  

### charamatrix.py
Charamatrix is the class containing the informations.  
It can do exporting .txt/.aas and loading .aas

### lists.names.py
An example on how to use it with multiple images.  
Please edit before using, as the file names are hard-coded.  

#### Other folders:

###Animal card maker
Takes the card base and inserts 16x16 animal and foods pngs in it to make an **ANSIART** card.  
(Can insert name or not)  
Using nearest_detector.py  (colored ▄▀█▓▒░) + characters for the name

### Basic BWreader
Takes an inage in input and outputs a **PASTEABLE** grayscale image with ▄▀█▓▒░#─  
It needs to be input the precise colors to recognise them. This means **the original image needs to be converted to 5-colors grayscale**!
It squishes two vertical pixels into one character.  

### Cards maker
Same as animal card, except it doesn't take images, but makes a set of **ANSIART** cards with Diamonds, Hearts, Spades and Spikes.  
Does not produce Jake, Queen, Kings or Jokers (maybe with Animal card maker).
Using nearest_detector.py  (colored ▄▀█▓▒░) + special characters ♥♦♣♠

### Color Reader for forums
Takes an image and transforms it into block art with color BBCODE **FOR FORUMS USE** (usually too heavy to post).  
Only uses ▄▀█─ with [color=#ff5959]▀▄▄[/color] markers

### Examples
Some small png images converted to ANSIART trough nearest_detector.py 

### Image to uniChar
Using more weird unicode characters, tries to transform a black-and-white image into a black-and-white unicode shape made up of characters.  
Algorithm is not very good (counts how many pixels are the same between two possibilities).
Uses PIL  

### Irma animation
Four-images animation and python script to read it.

### Nearest BWreader
Same as Basic BWreader  
Takes an inage in input and outputs a **PASTEABLE** grayscale image with ▄▀█▓▒░#─  
It is not working well, it is not using luminance but RBG mean to try to guess and approach colors. No need to convert the original image! Well, better convert it anyway to make it look better.  
It squishes two vertical pixels into one character.  
