####################################################################################
# Project           : Call Stack Example
#
# Program name      : abcdCallStack.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240627
#
# Purpose           : An example of the stack to illustrate how they work
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()