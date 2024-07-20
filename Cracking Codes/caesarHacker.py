# Caesar Hacker

message = 'vQFUbSWLQJnDQGnGHFUbSWLQJnLVnYHUbnFRROo'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound
            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            # Append the decrypted symbol
            translated += SYMBOLS[translatedIndex]
            
        else:
            # Append symbol without encrypting/decrypting
            translated += symbol

    print('Key #%s: %s' % (key, translated))
