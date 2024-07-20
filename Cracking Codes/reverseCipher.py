# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = '.daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    print('i is', i, ', message[i] is', message[i], ', translated is', translated)
    i -= 1

print(translated)
