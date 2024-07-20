# Transposition Cipher Decryption

import math, pyperclip

def main():
    myMessage = ('Incen,m  emuaogfeerg ptdie rwh \' p iooor c ntssioytr w '
                 'say so swo\'ttnvonot.mv eusau o  uheoorr nrtlyhrooivisitnhuoe u')
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    print(plaintext + '|-end-|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns

    column, row = 0, 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and
                                         row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    
    return ''.join(plaintext)

# If transpositionDecrypt.py is run (instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()
