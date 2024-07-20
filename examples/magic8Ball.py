####################################################################################
# Project           : Magic 8 Ball
#
# Program name      : magic8Ball.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240701
#
# Purpose           : Magic 8 Ball example
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])