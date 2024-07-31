####################################################################################
# Project           : All My Cats
#
# Program name      : allMyCats.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240628
#
# Purpose           : Working with Lists
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames += [name]

print('The cat names are:')
for name in catNames:
    print(' ' + name)