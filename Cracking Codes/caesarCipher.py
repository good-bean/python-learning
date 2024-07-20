# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

message = 'Encrypting and decrypting is very cool!'
key = 43
mode = 'encrypt'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)
        
        translated += SYMBOLS[translatedIndex]
    else:
        translated += symbol

print(translated)
pyperclip.copy(translated)
