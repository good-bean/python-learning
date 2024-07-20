####################################################################################
# Project           : Selection Sort Algorithm Example
#
# Program name      : selectionSort.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240618
#
# Purpose           : Study the selection sort algorithm and understand it better.
#                     This algorithm has a time complexity of O(n^2)
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
# 20240619    flaneryb     1      Added comments for further study and comparison
#
####################################################################################

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # in other languages this would be [for (int i = 0; i < arr.length; i++)]
        min = i # make current iteration minimum
        for j in range(i+1, len(arr)): # select next item to compare to i
            if arr[min] > arr[j]:
                min = j # make the current j iteration min if it is less than current i
        arr[i], arr[min] = arr[min], arr[i] # swap values in these positions

        new_arr.append(arr[i]) # append the minimum overall to the next available position
    return new_arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)
                