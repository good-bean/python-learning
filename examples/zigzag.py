####################################################################################
# Project           : Zigzag
#
# Program name      : zigzag.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240628
#
# Purpose           : Zigzag program.
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.005)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()