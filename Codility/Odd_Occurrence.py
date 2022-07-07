# A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of
# the array can be paired with another element that has the same value, except for one element that is left unpaired.
#
# For example, in array A such that:
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# sort the array, test equality b2n consecutive elements
# Increament index by 2 Odd element

def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort() #Sort the list in Ascending
    for i in range (0, len(A)-1, 2):
        if A[i] != A[i+1]:
            return A[i]
    return A[-1] #If it's a negative integer
