import subprocess, re
import urllib.request as requests
import threading
commands = [['arp', '-a'],['netstat'],['systeminfo']]
ports = ['443','19005','22','17775','80','15182','5060','5341','53','4978','1723','4718','8080','4207','21','2777','25','2350','4567','2328','3389','2200','8081','1856','8000','1841','110','1630','23','1418','10000','1396','81',
          '1228','8082','1228','5000','1208','445','1072','143','1024','111','957','7547','893','135','873','587','846','139','818','28960','813','29900','804','18067','803','27374','801','1024','747','30005','711','7676','705',
          '389','691','1026','678','4444','661','1025','628','1027','604','20','588','1050','555','1028','539','5678','533','1029','526','1863','507','8594','490','3783','482','1002','473','4664','472','37','455','4']
raw = ''
for command in commands:
    raw += subprocess.check_output(command).decode()
valid = '0123456789:.-'
ips = []
for i in range(len(raw)):
    if raw[i] in valid:
        ip = ''
        while raw[i] in valid:
            ip += raw[i]
            i+=1
        result = True
        match_obj = re.search( r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
        if  match_obj is None:
            result = False
        else:
            for value in match_obj.groups():
                if int(value) > 255:
                    result = False
                    break
        if result: ips.append(ip)

def test(port, ip):
    try:
        addr = 'http://'+ip+':'+port
        with requests.urlopen(requests.Request(addr)) as response:
            print('[+]',addr)
        print(ip+port)
    except Exception as e:
        print('.', end='')



for ip in ips:
    for port in ports:
        thread = threading.Thread(target=test, args=(ip, port))
        thread.start()
print('done!')
