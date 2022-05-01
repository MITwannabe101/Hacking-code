import os
import sys

class Executor:
    def __init__(self, mode='c'):
        self.cmd = None
        self.mode = 'c'
        if mode == 'k':
            self.mode = mode
        os.system(f'cmd /c "color 02"')
    
    def __call__(self, cmd):
        self.cmd = cmd.strip()
        if self.cmd == '^C':
            if self.mode=='k':
                print('\nExiting cmd prompt now...')
            sys.exit(0)
        return self.beautify(self.exec())
        
    def exec(self):
        return os.system(f'cmd /{self.mode} "{self.cmd}"')

    def beautify(self, text):
        for i in range(len(text)):
            if text[i] != '\\':
                sys.stdout.write(text[i])
                sys.stdout.flush()
            else:
                i += 1
                if text[i]=='n': print('')
                if text[i]=='r': continue
                else:
                    sys.stdout.write('\\')
                    sys.stdout.flush()
       

if __name__ == '__main__':
    exec = Executor('k')
    while True:
        try:
            exec(input(f'(base) {os.getcwd()}>'))
        except Exception as e:
            print(e)
