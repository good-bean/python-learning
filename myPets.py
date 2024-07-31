####################################################################################
# Project           : My Pets
#
# Program name      : myPets.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240701
#
# Purpose           : Working with Lists
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')