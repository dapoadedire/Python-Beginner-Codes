logins = {}
print('Welcome to the simplest key-value database')
while True:
    print('What do you want to do?')
    print('Enter P to [P]ut, G to [G]et or L to [L]ist')
    print('Or enter Q to [Q]uit')
    action = input()
    if action == 'P':
        name = input('Enter name: ')
        password = input('Enter password: ')
        logins[password] = name
    elif action == 'G':
        password = input('Enter password: ')
        if not password in logins:
            print('No such key')
        else:
            print('Your data: %s' % logins[password])
    elif action == 'L':
        print('DB contents:')
        print(logins)
    elif action == 'Q':
        print('Bye')
        break
