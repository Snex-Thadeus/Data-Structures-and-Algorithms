# Write a function:
# def solution(A)
# that, given a non-empty array A of N integers, returns the maximal result that can be achieved on the board represented by array A.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A):
    # write your code in Python 3.6
    lenA = len(A)
    if lenA == 0:
        return 0

    dp = [0] * lenA
    dp[0] = A[0]
    for i in range(1, lenA):
        j = i - 1
        maxBefore = -math.inf
        # check for the max value that can be achived using the current element and any of the last six positions
        while j >= 0 and j >= i - 6:
            maxBefore = max(maxBefore, dp[j] + A[i])
            j -= 1
        dp[i] = maxBefore
    return dp[lenA - 1]  # return the max value that can be achieved where the last position is included (lenA-1)