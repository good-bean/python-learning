# def factorial(n):
#     match n:
#         case 0:
#             return 1
#         case 1:
#             return 1
#         case 2:
#             return 2
#         case _:
#             pass
    
#     return n * factorial(n - 1)

# print(factorial(10))

import math

n = 8

for i in range(n+1):
    print('The factorial of %s is : %s' % (i, math.factorial(i)))
