####################################################################################
# Project           : Counting Sort Algorithm Example
#
# Program name      : countingSort.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240705
#
# Purpose           : Study the counting sort algorithm and understand it better.
#                     This algorithm has a time complexity of O(n+k)
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
    
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1
    
    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)