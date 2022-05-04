import sys
import urllib.parse as parse
import urllib.request as request


class HTMLParser:
    def __init__(self, html):
        self.html = html
        self.indentation = '\t'
        self.num_indents = 0
        self.parse()

    def parse(self):
        i = 0
        inStr = False
        numbrackets = 0
        for i in range(0, len(self.html)):
            if self.html[i] == '(':
                numbrackets += 1
            if self.html[i] == ')':
                numbrackets -= 1
                
            if self.html[i] == '<':
                x = i
                while self.html[x] != '>':
                    x += 1
                if self.html[i+1] == '/':
                    self.num_indents -= 1
                else:
                    self.num_indents += 1
                print()
                for _ in range(self.num_indents):
                    print(self.indentation, end='')
                print(self.html[i], end='')
                
            elif self.html[i] == ';' and inStr == False and numbrackets == 0:
                print(self.html[i], end='')
                print('\n')
                for _ in range(self.num_indents):
                    print(self.indentation, end='')
                    
            elif self.html[i] == '"':
                inStr = not inStr
                print(self.html[i], end='')

            else:    
                print(self.html[i], end='')

if __name__ == '__main__':
  url = 'http://www.google.com'
  with request.urlopen(url) as response:
      response = str(response.read())[2:-1]
      print(response, '\n\n\n\n\n\n')
      HTMLParser(response)

