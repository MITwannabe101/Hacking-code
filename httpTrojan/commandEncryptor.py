import random

def encrypt(json):
      string = ''
      #add random characters
      for i in range(0, len(json)):
          string += json[i]
          string += chr(random.randint(32, 60))
      print(string)
      strUTF8 = str(string.encode("utf-8"))[2:1]
      print(strUTF8)
      strB2 = ''.join(format(ord(i), '08b') for i in strUTF8) 

      html = '<!doctype html><body><h3>'+strB2+'</h3></body></doctype>'
      return html

