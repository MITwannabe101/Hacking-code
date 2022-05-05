import urllib.parse as parse
import urllib.request as request

import json

class HTMLclient:
    def __init__(self, commandlink):
        self.commandlink = commandlink

        
    def recievecommands(self, commandlink=''):
        """GET request to web page to get commands"""
        if commandlink=='': commandlink=self.commandlink #makes sure there is link
        
        #gets html
        with request.urlopen(commandlink) as response:
            html = response.read().decode() #recieved commands

        """hidden json:
            1) add random chareceter after every charecter in json- e.g {"a":"b"} -> A{B"Fa("G:L"XbK"A}
            2) encrypt into base64
            3) put in html""""
            
        #extracts hidden json
        Hjson_start, Hjson_end = 0, 0 #hidden jason start and end
        while html[Hjson_start] != '{': Hjson_start += 1
        while html[Hjson_end] != '}': Hjson_end -= 1
        Hjson = html[Hjson_start:Hjson_end+1]
        
        #gets json from hidden json
        jsonStr = ''
        for i in range(0, len(Hjson), 2):
                jsonStr += str(Hjson[i])
        
        #converts jsonStr to dictionary
        commands = json.loads(jsonStr)
        
        return commands

if __name__ == '__main__':
    #x = HTMLclient('https://api.wheretheiss.at/v1/satellites/25544')
    #print(x.recievecommands())
