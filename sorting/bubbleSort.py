####################################################################################
# Project           : Bubble Sort Algorithm Example
#
# Program name      : bubbleSort.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240705
#
# Purpose           : Study the bubble sort algorithm and understand it better.
#                     This algorithm has a time complexity of O(n+k)
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)