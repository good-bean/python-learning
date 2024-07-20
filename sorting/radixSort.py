####################################################################################
# Project           : Radix Sort Algorithm Example
#
# Program name      : radixSort.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240619
#
# Purpose           : Study the radix sort algorithm and understand it better.
#                     This algorithm has a time complexity of O(wn)
#                     From what I know, it involves Counting Sort algorithm
#                     Worth studying before diving into radix
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

def radixSort(arr):
    radix_array = [[], [], [], [], [], [], [], [], [], []]
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:

        while len(arr) > 0:
            val = arr.pop()
            radix_index = (val // exp) % 10
            radix_array[radix_index].append(val)
        
        for bucket in radix_array:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)
        
        exp *= 10
    
    return arr

def main():
    arr = [492, 93, 325, 592, 302, 89, 508, 547, 41, 65]
    print("Original array:", arr)
    print("Sorted array:", radixSort(arr))

main()