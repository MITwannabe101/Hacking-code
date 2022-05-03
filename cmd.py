import os
import sys

class Executor:
    def __init__(self, mode='c'):
        self.cmd = None
        self.mode = 'c'
        if mode == 'k':
            self.mode = mode
        os.system('cmd /c "color 02"')
    
    def __call__(self, cmd):
        self.cmd = cmd.strip()
        if self.cmd == '^C':
            if self.mode=='k':
                print('\nExiting cmd prompt now...')
            sys.exit(0)
        return self.beautify(self.exec())
        
    def exec(self):
        return os.system('cmd /%s "%s"'% (self.mode, self.cmd))

    def beautify(self, text):
        string = ''
        for i in range(len(text)):
            if text[i] != '\\':
                string.append(text[i])
            else:
                i += 1
                if text[i]=='n': string.append('\n')
                if text[i]=='r': continue
                else:
                    string.append('\\')
        return string
       

if __name__ == '__main__':
    exec = Executor('k')
    while True:
        try:
            print(exec(input('%s>' % os.getcwd())))
        except Exception as e:
            print(e)
