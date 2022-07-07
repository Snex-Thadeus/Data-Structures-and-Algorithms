# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine
# the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the
# worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.
#
# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
#
# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating
# the list [3, 2, 4, 1] produces [1, 3, 2, 4].
#
# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

def min_times_of_rotation(nums):
    n = len(nums)
    start = 0
    end = n-1
# index of minimum of the array would be equal to number to rotation
# Only the minimum value will be less than its previous value
# Binary search
    while start<=end:
        mid = start+(end-start)//2
# Calculating the previous(prev) index of mid
        prev = mid-1
# Checking if mid is minimum
        if nums[mid]<nums[prev]:
            return mid
# if we didn't find min value, then change limits
        elif nums[mid]<nums[start]:
            end = mid-1
        elif nums[mid]>nums[end]:
            start = mid+1
        else:
            return 0

x = [5, 6, 9, 0, 2, 3, 4]
print(min_times_of_rotation(x))

x = [6,7,8,9,0,1,2,3,4,5]
print(min_times_of_rotation(x))