from sys import argv 
import re 
script = argv[0]
filename = argv[1]
#filename = argv 

#with open (filename, "r+") as f:
    #text = f.read()
    #text = re.sub('7', 'k', text)
    #f.seek(0)
    #f.write(text)
    #f.truncate()

with open (filename, "r+") as f:
   text = f.read()
   text = text.translate(str.maketrans('0', '>'))
   text = text.translate(str.maketrans('1', '>'))
   text = text.translate(str.maketrans('2', '>'))
   text = text.translate(str.maketrans('3', '>'))
   text = text.translate(str.maketrans('4', '>'))
   text = text.translate(str.maketrans('5', '>'))
   text = text.translate(str.maketrans('6', '>'))
   text = text.translate(str.maketrans('7', '>'))
   text = text.translate(str.maketrans('8', '>'))
   text = text.translate(str.maketrans('9', '>'))
   f.seek(0)
   f.write(text)
   f.truncate()   


