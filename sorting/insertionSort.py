####################################################################################
# Project           : Insertion Sort Algorithm Example
#
# Program name      : insertionSort.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240619
#
# Purpose           : Study the insertion sort algorithm and understand it better.
#                     This algorithm has a time complexity of O(n^2)
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

def insertionSort(arr):
    for i in range(1, len(arr)): # start iteration i from position 1
        key = arr[i] # key is position 1 value
        j = i - 1 # interation j is i - 1 (first time around it is 0)

        while (j >= 0) and (key < arr[j]): # while j is >= 0 and key value is less than value at j
            arr[j+1] = arr[j] # swap next j value with current j value
            j -= 1 # go up the line until < 0
        arr[j+1] = key # swap j value at 0 with key value
        # print(arr)

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in arr:
    print(f"{i} ", end='')