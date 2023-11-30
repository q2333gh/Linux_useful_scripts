import os

def enable_proxy():
    print('Enabling proxy...')
    with open('/etc/environment', 'r') as file:
        lines = file.readlines()

    with open('/etc/environment', 'w') as file:
        for line in lines:
            if line.startswith('# http_proxy'):
                file.write(line[1:])
            elif line.startswith('# https_proxy'):
                file.write(line[1:])
            else:
                file.write(line)
    print('Proxy enabled.')

def disable_proxy():
    print('Disabling proxy...')
    with open('/etc/environment', 'r') as file:
        lines = file.readlines()

    with open('/etc/environment', 'w') as file:
        for line in lines:
            if line.startswith('http_proxy'):
                file.write('#' + line)
            elif line.startswith('https_proxy'):
                file.write('#' + line)
            else:
                file.write(line)
    print('Proxy disabled.')

if __name__ == "__main__":
    command = input('Enter command (enable/disable): ')
    if command == 'enable':
        enable_proxy()
    elif command == 'disable':
        disable_proxy()
    else:
        print('Invalid command. Use "enable" or "disable".')

