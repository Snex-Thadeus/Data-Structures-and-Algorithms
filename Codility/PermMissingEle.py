# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)],
# which means that exactly one element is missing.
# Your goal is to find that missing element.
# For example, given array A such that:
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
# Unique elements
# Largest element value is equal to N+1
# smallest element is 1
# Brute Force: for i=1 to N+1, loop thro the array and test if we find i
def solution(A):
    if (len(A) == 0):
        return 1
    A.sort()

    for i in range(0, len(A)):
        if A[i] != i+1:
            return i+1
    return (len(A)+1)