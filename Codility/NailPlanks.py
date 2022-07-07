# example case ([1, 4, 5, 9], [4, 5, 9, 10], [4, 6, 7, 8, 2]) -> -1
# example case [[1, 4, 5, 9], [4, 5, 9, 10], [4, 6, 7, 8, 2]] ->4
# ([1, 4, 5, 8], [4, 5, 9, 10], [10, 2, 7, 4, 8]) -> 2
# Write a function:
#
# def solution(A, B, C)
#
# that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.
#
# If it is not possible to nail all the planks, the function should return −1.


# %100 correct, %100 performance
def solution(A, B, C):
    # write your code in Python 3.6

    N = len(A)
    M = len(C)
    largestPos = max(A + B + C)

    low = 1
    high = N

    lastValid = -1
    while (low <= high):
        mid = (low + high) // 2

        nailedPositions = [0] * (largestPos + 1)
        for i in range(mid):
            nailedPositions[C[i]] = 1

        for i in range(1, largestPos + 1):
            nailedPositions[i] += nailedPositions[i - 1]

        possible = True
        for a, b in zip(A, B):
            # no nail has been nailed in interval [a,b].
            if nailedPositions[b] - nailedPositions[a - 1] == 0:
                possible = False
                break

        if possible:
            lastValid = mid
            high = mid - 1
        else:
            low = mid + 1

    return lastValid