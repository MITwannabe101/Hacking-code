import urllib.parse as parse
import urllib.request as request

class HTMLclient:
    def __init__(self, webserver, commandlink, outcomelink):
        self.webserver = webserver
        self.commandlink = commandlink
        self.outcomelink = outcomelink
        
    def recievecommands(self, webserver=self.webserver, commandlink=self.commandlink):
        """GET request to web page to get commands"""
        with request.urlopen('%s%s' % (webserver, commandlink)) as response
            rawcommands = response.read()[2:-1]
        commands = self.parsecommands(rawcommands)
        
    def gettag(self, rawcommands, i):
            x = i
            while rawcommands[x] != '>': x += 1 #find end of tag
            tag = {'tagtype' : '', 'endtag' : False, 'tagend' : x}
            tag['tagtype'] = rawcommands[i+1: x-1]
            if rawcommands[i+1] == '/':
                tag['endtag'] = True
                tag['tagtype'] = rawcommands[i+2: x-1].lower()
            return tag
    
    def getcontent(self, rawcommands, i):
        x = i
        while rawcommands[x] != '<':
            x += 1
        return rawcommands[i:x], x
    
    def parsecommands(self, rawcommands):
        """h1- write inside to disk
           h2- read file from disk
           h3 -run file on disk
           h4- inside h1/h2, defines file name"""
        unformattedcommands = {}
        numcommands =  {'h1' : 0,'h2' : 0,'h4' : 0}
        loc = None
        i = 0
        cap = len(rawcommands) #the length of the raw commands
        while i<cap:
            tag  = self.gettag(rawcommands, i) #returns dictionary of tag type
            i = tag['tagend'] #update i to skip tag
            if tag['endtag'] == True and tag['tagtype'] != :
                loc = None #not a command anymore
                continue #loop round to to next tag
            else:
                if tag['tagtype'] == 'h4': #file name command
                    unformattedcommands[loc][0], i = self.getcontent(rawcommands, i) #gets contents of tag
                else: #normal command
                    loc = str('%s%s' %(tag['tagtype'], numcommands[tag['tagtype']])) #creates string describing command
                    if tag['tagtype'] == 'h1':
                        unformattedcommands[loc][1], i = self.getcontent(rawcommands, i) #1 is file content, 0 is file name
                    if tag['tagtype'] == 'h2'  or tag['tagtype'] == 'h3':
                        unformattedcommands[loc] = []
                        _, i = 
                    else:
                        unformattedcommands[loc], i = self.getcontent(rawcommands, i)  #creates empty location in the commands dictionary
                    numcommands[tag['tagtype']] += 1 #increases the number of tags of it's type