# A practice in writing code to find a value's factors
# Also practice in finding greatest common factor/divisor

# Any non-zero whole number times 0 equals 0 so it is true
# that every non-zero whole number is a factor of 0

# The GCF (or GCD or HCF) of a set of whole numbers is the
# largest positive integer that divides evenly into all
# numbers with zero remainder.

# For example, the set of numbers 18, 30, and 42
# the GCF is 6

# k x 0 = 0 so, 0 / k = 0 for any whole number k
# For example, 5 x 0 = 0, so it is true that 0 / 5 = 0
# GCF(5,0) = 5 and more generally GCF(k,0) = k for any
# whole number k.
# However, GCF(0,0) is undefined.

# finding factors
def factor(n):
    fact_list = []
    for i in range(1, n+1):
        if n % i == 0:
            fact_list.append(i)
    return fact_list

def print_factor_list(fact_list):
    for i in fact_list:
        if i != fact_list[-1]:
            print(i, end=', ')
        else:
            print(i)

factor_number = 24
list_of_facts_1 = factor(factor_number)
print('List of factors for the number %s : ' % (factor_number), end='')
print_factor_list(list_of_facts_1)

factor_number = 30
list_of_facts_2 = factor(factor_number)
print('List of factors for the number %s : ' % (factor_number), end='')
print_factor_list(list_of_facts_2)

intersected = list(filter(lambda x: x in list_of_facts_1, list_of_facts_2))

print('The common factors of both are : ', end='')
print_factor_list(intersected)

print('The greatest common factor is : %s' % (max(intersected)))
