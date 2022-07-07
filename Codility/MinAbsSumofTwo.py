# Let A be a non-empty array consisting of N integers.
# The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.
# For example, the following array A:
#   A[0] =  1
#   A[1] =  4
#   A[2] = -3
# has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
# The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
# The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
# The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2.
# The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
# The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1.
# The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6.
# Write a function:
# def solution(A)
# that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.

# example case [-3,-1,1,4]
import math


def solution(A):
    # write your code in Python 3.6
    A.sort()
    lenA = len(A)
    if lenA == 1:
        return abs(2 * A[0])

    # find the max value that j can take
    j = 0
    while j < lenA and A[0] + A[j] < 0:
        j += 1
    j -= 1

    minAbsVal = math.inf
    for i in range(lenA):
        while j >= 0 and A[i] + A[j] > 0:
            j -= 1

        minAbsVal = min(minAbsVal, abs(A[i] + A[j]))  # the possible min abs for negatives
        if j + 1 != lenA:  # A[i]+A[j]>=0; then A[i+1]+A[j]>=0
            minAbsVal = min(minAbsVal, abs(A[i] + A[j + 1]))  # the possible min abs for positives.

        # If A[i]+A[j]>0;  then it means j is negative and we should not increment i anymore; since otherwise it would only worsen the result
        # If A[i]+A[j]==0, then we already found the minimum.
        if A[i] + A[j] >= 0:
            break

    return minAbsVal
