import subprocess, re
import socket
import threading
from time import sleep
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ports = [20,21,22,23,25,37,53,80,81,110,111,135,139,143,389,442,443,445,445,472,473,482,490,507,526,533,539,555,587,588,604,628,661,678,691,705,711,747,801,803,804,813,818,846,873,893,
         957, 1002, 1024, 1024, 1025, 1026, 1027, 1028, 1029, 1050, 1072, 1208, 1228, 1228, 1396, 1418, 1630, 1723, 1841, 1856, 1863, 2200, 2328, 2350, 2777, 3389, 3783, 4207, 4444, 4567, 4664, 4718, 4978, 5000, 5060, 5341, 5678, 7547, 7676, 8000, 8080, 8081, 8082, 8594, 10000, 15182, 17775, 18067, 19005, 27374, 28960, 29900, 30005]
class IPExtractionUnit:
    def __init__(self, *commands):
        self.commands = [command.split() for command in commands]

    def __call__(self):
        raw = ''
        try:
            with open('ips.txt', 'r') as file:
                raw += file.read()
        except:
            pass
        for command in self.commands:
            try: raw += subprocess.check_output(command).decode()
            except: pass
        valid, ips, i = '0123456789:.', [], 0
        while i < len(raw):
            if raw[i] in valid:
                ip = ''
                while raw[i] in valid:
                    ip += raw[i]
                    i+=1 #gets ip adress
                result = True
                match_obj = re.search( r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip.split(':')[0])
                if  match_obj is None:
                    result = False
                else:
                    for value in match_obj.groups():
                        if int(value) > 255:
                            result = False
                            break
                if result and ip not in ips:
                    if len(ip.split(':')) > 1 and ip.split(':')[-1]: ips.append((ip.split(':')[0], int(ip.split(':')[1])))
                    else: ips.append((ip.split(':')[0], None))
            i+= 1
        return set(ips)



class IPTestingUnit:
    def __init__(self, addrs, ports):
        self.addrs = addrs
        self.ports = ports
        self.open = []

    def run(self):
        print('[^] initiating testing')
        threads = []
        for addr in self.addrs:
            if addr[1] != None:
                threads.append(threading.Thread(target=self.test, args=(addr[0], addr[1])))
            else:
                for port in self.ports:
                    threads.append(threading.Thread(target=self.test, args=(addr[0], port)))
        num_threads = len(threads)
        while len(threads) > 0:
            try:
                threads.pop().start()
            except RuntimeError:
                MAX_THREADS = threading.active_count()
                for i in range(len(threads)):
                    if i % MAX_THREADS == 0:
                        print('exceeded max threads')
                        sleep(5)
                        print('finished operation: exceeded max threads')
                    threads.pop().start()
        self.display()
        
    def display(self):
        for found in self.open:
            print('[*] {}:{}'.format(found[0], found[1]), end='')
            for _ in range(25- len('[*] {}:{}'.format(found[0], found[1]))):
                print(' ', end='')
            if type(found[2]) == None:
                print('service-not found')
            else:
                print('service- {}'.format(found[2][0]))
            if found[3] is not None:
                print(found[3].decode())
            
    def test(self, addr, port=80):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((addr,port))
        if result == 0:
                try: banner = sock.recv(4096)
                except socket.timeout: banner = None
                try: hostname = socket.gethostbyaddr(addr)
                except: hostname = None
                try: self.open.append([addr, port, list(hostname), banner])
                except: pass
        sock.close()
        return None


                
IPtester = IPTestingUnit(IPExtractionUnit('arp -a', 'netstat', 'systeminfo')(), ports)
IPtester.run()

