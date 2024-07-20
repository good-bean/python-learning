####################################################################################
# Project           : Binary Search Algorithm Example
#
# Program name      : binarySearch.py
#
# Author            : Bridget Flanery (flaneryb)
#
# Date created      : 20240618
#
# Purpose           : Study the binary search algorithm and understand it better.
#                     This algorithm has a time complexity of O(lgn)
# 
# Revision History  :
# 
# Date        Author       Ref    Revision (Date in YYYYMMDD format)
#
####################################################################################

def binSearch(arr, left, right, target):
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] > target:
            return binSearch(arr, left, mid - 1, target)
        
        return binSearch(arr, mid + 1, right, target)
    # =================================================
    # NON-RECURSIVE METHOD IS SIMPLY USING A WHILE LOOP
    # =================================================
    # left = 0
    # right = len(arr) - 1

    # while left <= right:
    #     mid = (left + right) // 2

    #     if arr[mid] == target:
    #         return mid
        
    #     if arr[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    return -1

nums = [1, 2, 5, 7, 8, 9]
target = 2
n = len(nums)
result = binSearch(nums, 0, n - 1, target)

if result != -1:
    print(f"Value {target} found at index {result}")
else:
    print("Target not found in array.")