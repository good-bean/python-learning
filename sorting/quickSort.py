####################################################################################
# Project           : Quicksort Algorithm Example
#
# Program name      : quickSort.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240621
#
# Purpose           : Study the quicksort algorithm and understand it better.
#                     This algorithm has a time complexity of O(nlgn)
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
# 20240621    flaneryb     1      Added comments for further study and comparison
# 02242024    flaneryb     2      No you did not. That is a comment from another file
#
####################################################################################

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [80, 57, 31, 56, 126, 137, 122, 3, 43, 93]
quicksort(my_array)
print("Sorted array:", my_array)