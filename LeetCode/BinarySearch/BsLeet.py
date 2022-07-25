# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given
# target value.
# If target is not found in the array, return [-1, -1].

def findFirstOccurrence(nums, target):
    # Left snd right pointers
    left, right = 0, len(nums) - 1
    # Index of first occurrence
    firstOccurrence = -1
    # Loop until the two pointers meet
    while left <= right:
        # Middle index
        middle = left + (right - left) // 2
        # Check if we have found the value
        if target == nums[middle]:
            firstOccurrence = middle
            right = middle - 1
        # If the target is less than the element
        # at the middle index
        elif target < nums[middle]:
            right = middle - 1
        # If the target is greater than the element
        # at the middle index
        else:
            left = middle + 1
    return firstOccurrence


def findLastOccurrence(nums, target):
    # Left snd right pointers
    left, right = 0, len(nums) - 1
    # Index of first occurrence
    lastOccurrence = -1
    # Loop until the two pointers meet
    while left <= right:
        # Middle index
        middle = left + (right - left) // 2
        # Check if we have found the value
        if target == nums[middle]:
            lastOccurrence = middle
            left = middle + 1
        # If the target is less than the element
        # at the middle index
        elif target < nums[middle]:
            right = middle - 1
        # If the target is greater than the element
        # at the middle index
        else:
            left = middle + 1
    return lastOccurrence


def searchRange(nums, target):
    return [findFirstOccurrence(nums, target), findLastOccurrence(nums, target)]