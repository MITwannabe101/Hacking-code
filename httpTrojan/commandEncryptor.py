import random

def encrypt(json)
  while True:
      string = ''
      for i in range(0, len(json)):
          string += json[i]
          string += chr(random.randint(32, 90))
      enc = str(string.encode())[2:-1]
      html = '<!doctype="html"><h3><hr>'+enc+'</h3></doctype>'
      print(html)
