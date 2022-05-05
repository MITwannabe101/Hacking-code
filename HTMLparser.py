import urllib.parse as parse
import urllib.request as request

import json

class HTMLclient:
    def __init__(self, commandlink):
        self.commandlink = commandlink

        
    def recievecommands(self, commandlink=''):
        """GET request to web page to get commands"""
        if commandlink=='': commandlink=self.commandlink
        with request.urlopen(commandlink) as response:
            rawcommands = response.read().decode()
        commands = json.loads(rawcommands)
        return commands

if __name__ == '__main__':
    x = HTMLclient('https://api.wheretheiss.at/v1/satellites/25544')
    print(x.recievecommands())
