####################################################################################
# Project           : Exception Handling Example
#
# Program name      : zeroDivide.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240627
#
# Purpose           : An example of handling exceptions.
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

def spam(divideBy):
    try:
        return 42 // divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
