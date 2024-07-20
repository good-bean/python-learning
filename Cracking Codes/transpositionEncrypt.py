# Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = ('If someone\'s voice is overpowering yours, it\'s important'
                 ' to turn down their volume so you can hear your own thoughts.')
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return ''.join(ciphertext)

# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()
