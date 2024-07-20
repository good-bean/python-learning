attempt = 0

while True:
    print('Enter your password: ', end='')
    typedPassword = input()
    if typedPassword == 'swordfish':
        print('Access Granted.')
        break
    else:
        print('Access Denied.')
    attempt += 1
    if attempt >= 3:
        print('You have reached the max allowable attempts. Restart and try again.')
        break
    print('Try again. ')

print('Done.')
