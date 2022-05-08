import random
import base64
import string

def encrypt(plaintext: str) -> str:
    #add random charecters to plaintext- still no encryption
    randomtext = ''
    for i in range(len(plaintext)):
        randomtext += plaintext[i]
        randomtext += chr(random.randint(33, 126))
    #convert randomtext to binary
    binarytext = ''.join(format(ord(i), '08b') for i in randomtext)
    binarytext = binarytext
    #convert binary to base64
    base64text = base64.b64encode(binarytext.encode('utf-8'))
    #adds random charecters to base64
    randombase64text = ''
    for i in range(len(str(base64text))):
        randombase64text  += str(base64text)[i]
        randombase64text  += chr(random.randint(33, 126))
    html = f'<!doctype html><body>{randombase64text}</body></doctype>'
    return html

def decrypt(html : str) -> str:
    #remove html
    base64text = html[21:-17]
    #removes random charecters
    base64text_norandom = base64text[2:-1:2].encode('utf-8')[1:]
    ###print('base64text    ', base64text_norandom)
    #decode from base64
    binarytext = base64.b64decode(base64text_norandom).decode()
    ###print('binary:   ', binarytext)
    #converts from binary to text
    randomtext = ''.join(chr(int(binarytext[i*8:i*8+8],2)) for i in range(len(binarytext)//8))
    #extract plaintext
    plaintext = randomtext[::2]
    return plaintext