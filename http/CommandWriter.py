from Encryptor import *

def writecommands():
    computer = input('>')
    commands = get_commands(computer)
    commands = commands.replace('\'', '"')
    with open(f'Server/{computer.lower()}.txt', 'w', encoding='utf-8') as file:
        file.write(encrypt(commands))

def get_commands(computer):
    commands = {}
    while True:
        key = input(f'{computer}>')
        if key == '^C': break
        values = []
        while True:
            value = input(f'{computer}:{key}>')
            if value == '^C': break
            values.append(value)
            commands[key] = values
    return str(commands)

writecommands()
