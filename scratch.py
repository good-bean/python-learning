####################################################################################
# Project           : Lambda Exploration
#
# Program name      : scratch.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240712
#
# Purpose           : An exploration into lambda functions
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

# from functools import reduce
# import pprint

# ADD 15 AND MULTIPLY TWO NUMBERS TOGETHER
# add_15 = lambda x: x + 15
# multiply = lambda x, y: x * y
# print(add_15(10))
# print(multiply(6, 8))

# PERFORM MULTIPLICATION WITH PASSED IN NUMBER
# def multiplied_by(num):
#     return lambda x: x * num
# double = multiplied_by(2)
# triple = multiplied_by(3)
# quadruple = multiplied_by(4)
# quintuple = multiplied_by(5)

# print(double(15))
# print(triple(15))
# print(quadruple(15))
# print(quintuple(15))

# SORT LIST OF TUPLES
# grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# sorted_grades = sorted(grades, key=lambda index: index[1])

# print(sorted_grades)

# SORT LIST OF DICTIONARIES
# phone_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#               {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#               {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# sorted_phone_list = sorted(phone_list, key=lambda i: i['color'])

# pprint.pprint(sorted_phone_list)

# FILTER LIST OF INTEGERS
# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda x: (x % 2 == 0), integers))
# odds = list(filter(lambda x: (x % 2 == 1), integers))

# print(evens)
# print(odds)

# SQUARE AND CUBE EVERY NUMBER IN A LIST
# integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared = list(map(lambda x: x ** 2, integers))
# cubed = list(map(lambda x: x ** 3, integers))

# print(squared)
# print(cubed)

# CHECK IF A STRING STARTS WITH A SPECIFIC CHARACTER
# def check_for(char):
#     return lambda x: True if x.startswith(char) else False

# starts_with_P = check_for('P')
# starts_with_J = check_for('J')

# print(starts_with_P('Python'))
# print(starts_with_P('Java'))
# print(starts_with_J('Python'))
# print(starts_with_J('Java'))

# CHECK WHETHER A GIVEN STRING IS A NUMBER
# is_number = lambda x: True if x.isnumeric() else False

# print(is_number('5'))
# print(is_number('Five'))
# print(is_number('256'))
# print(is_number('Two-hundred'))
# print(is_number(str(4)))
# print(is_number(str(10)))

# FIBONACCI SERIES
# fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])

# print(fib(10))

# INTERSECTION OF TWO ARRAYS
# array_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_2 = [1, 2, 4, 8, 9]

# intersected = list(filter(lambda x: x in array_1, array_2))

# print('ORIGINAL ARRAYS')
# print('Array 1:', array_1)
# print('Array 2:', array_2)
# print()
# print('INTERSECTION ARRAYS')
# print(intersected)
