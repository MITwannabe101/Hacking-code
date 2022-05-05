import urllib.parse as parse
import urllib.request as request

import json

class HTMLclient:
    def __init__(self, commandlink):
        self.commandlink = commandlink

        
    def recievecommands(self, commandlink=self.commandlink):
        """GET request to web page to get commands"""
        with request.urlopen('%s' % commandlink) as response:
            rawcommands = response.read()[2:-1]
        commands = json.loads(rawcommands)
        return commands

if __name__ == '__main__':
    x = HTMLclient('https://api.wheretheiss.at/v1/satellites/25544')
    print(x.recievecommands())
