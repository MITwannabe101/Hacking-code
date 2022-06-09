import subprocess, re
import urllib.request as requests
import threading
from time import sleep
commands = [['arp', '-a'], ['route'], ['systeminfo'], ['netstat']]
ports = ['443','19005','22','17775','80','445','15182','5060','5341','53','4978','1723','4718','8080','4207','21','2777','25','2350','4567','2328','3389','2200','8081','1856','8000','1841','110','1630','23','1418','10000','1396','81',
          '1228','8082','1228','5000','1208','445','1072','143','1024','111','957','7547','893','135','873','587','846','139','818','28960','813','29900','804','18067','803','27374','801','1024','747','30005','711','7676','705',
          '389','691','1026','678','4444','661','1025','628','1027','604','20','588','1050','555','1028','539','5678','533','1029','526','1863','507','8594','490','3783','482','1002','473','4664','472','37','455','4']
def valid_ip(ip):
    result = True
    match_obj = re.search( r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip.split(':')[0])
    if  match_obj is None:
        result = False
    else:
        for value in match_obj.groups():
            if int(value) > 255:
                result = False
                break
    return result
raw = ''
for command in commands:
    try:
        raw += subprocess.check_output(command).decode()
    except:
        pass
print(raw)
valid = '0123456789:.-https'
ips = []
i=0
print('[^] extracting ips...')
while i < len(raw):
    if raw[i] in valid:
        ip = ''
        while raw[i] in valid:
            ip += raw[i]
            i+=1 #gets ip adress
        try:
            int(ip.split(':')[1])#checks if part after ip is a port
        except ValueError: #if not then is a type- httpas,http etc
            proto = ip.split(':')[1]
            ip = proto + chr(1) + ip.split(':')[0]
            if valid_ip(ip.split(chr(1))[-1]): print(ip)
        except IndexError:
            pass
        if valid_ip(ip.split(chr(1))[-1]) and ip not in ips:
            ips.append(ip)
    i+= 1
print(len(ips),'\n\nip adresses found\n',len(ports),'ports')





results = []
def test(ip, port, protocol='http'):
    try:
        addr = protocol+'://'+ip+':'+port
        print(addr)
        with requests.urlopen(requests.Request(addr)) as response:
            print(str('[+]',addr,'\n'))
    except Exception as e:
        print(e)
        results.append('.')

threads = []
print('[*] creating threads...')
for ip in ips:
    if ':' in ip:
        args = (ip.split(':')[0], ip.split(':')[1])
        if chr(1) in ip:
            args = (ip.split(chr(1))[-1].split(':')[0], ip.split(chr(1))[-1].split(':')[1], ip.split(chr(1))[0])
        threads.append(threading.Thread(target=test, args=args))
    else:
        for port in ports:
            args = (ip, port)
            if chr(1) in ip:
                args = (ip.split(chr(1))[-1], port, ip.split(chr(1))[0])
            threads.append(threading.Thread(target=test, args=args))
print('[*] created threads')
print(len(threads))
i = 0
for thread in threads:
    if i%50:
        thread.start()
        sleep(0.1)
    else:
        sleep(0.1)
    i+=1
print(*results)



