# An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.
# A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.
# For example, consider integer M = 6 and array A such that:
#     A[0] = 3
#     A[1] = 4
#     A[2] = 5
#     A[3] = 5
#     A[4] = 2
# There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).
# The goal is to calculate the number of distinct slices.
# Write a function:
# def solution(M, A)
# that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

# (6,[5,5,5,5,5,5,5,5,5,5])
# (6,[3,5,4,5,2])
# (6,[3,5,4,2,5,2])
##(6,[3,5,4,5,3,2]) -> should return 15

# Detected time complexity O(N)
def solution(M, A):
    # write your code in Python 3.6
    numberPositions = [-1] * (M + 1)
    N = len(A)
    distinctSlicesEndingAt = [0] * N
    newDistinctSliceBeginning = 0

    for i in range(N):
        # all element counts before the 1st position of a duplicate should become obsolete.
        # instead of making counts -1 each time meeting a new slice; do it lazily
        # check if the position is inside the boundaries of the current valid slice
        if numberPositions[A[i]] != -1 and numberPositions[A[i]] >= newDistinctSliceBeginning:
            newDistinctSliceBeginning = numberPositions[A[i]] + 1

        numberPositions[A[i]] = i;
        # add only itself + all the before(adding itself)
        # it turns out to be adding only the length of the slice (since we look sequntially e.g. 3 / 3,4 & 4 / 3,4,5 & 4,5 &5)
        distinctSlicesEndingAt[i] = i - newDistinctSliceBeginning + 1

    res = 0
    for sliceCount in distinctSlicesEndingAt:
        res += sliceCount
        if res > 1_000_000_000:
            res = 1_000_000_000
            break

    return res