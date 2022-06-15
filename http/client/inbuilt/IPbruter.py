import subprocess, re
import socket
import threading
from time import sleep
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ports = [443,19005,22,17775,80,445,15182,5060,5341,53,4978,1723,4718,8080,4207,21,2777,25,2350,4567,2328,3389,2200,8081,1856,8000,1841,110,1630,23,1418,10000,1396,81,1228,8082,1228,5000,1208,445,1072,143,1024,111,957,7547,893,
         135,873,587,846,139,818,28960,813,29900,804,18067,803,27374,801,1024,747,30005,711,7676,705,389,691,1026,678,4444,661,1025,628,1027,604,20,588,1050,555,1028,539,5678,533,1029,526,1863,507,8594,490,3783,482,1002,473,4664,472,37]
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
            if type(found[2]) == None:
                print('[*] {}:{} service- unable to identify'.format(found[0], found[1]))
            else:
                if type(found[2]) == None: #not empty
                    print('[*] {}:{} service- {}\\{}'.format(found[0], found[1], found[2][0], found[2][1]))
                else:
                    print('[*] {}:{} service- {}'.format(found[0], found[1], found[2][0]))

    def test(self, addr, port):
        sys.stdout.write('.')
        sys.stdout.flush()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((addr,port))
        sock.close()
        if result == 0:
                try: hostname = socket.gethostbyaddr(addr)
                except: hostname = None
                self.open.append((addr, port, hostname))
        return None


                
IPtester = IPTestingUnit(IPExtractionUnit('arp -a', 'netstat', 'systeminfo')(), ports)
IPtester.run()

