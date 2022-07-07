# Write a function:
# def solution(A, B)
# that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

# we have to search for the next one (next non-overlapping) whose ending is the least since least ending
# cannot be a worse choice than a smaller start with larger ending.
def solution(A, B):
    N = len(A)
    if N == 0:
        return 0
    count = 1
    i = 1
    curr_end = B[0]
    while i < N:
        if A[i] > curr_end:
            count += 1
            curr_end = B[i]
        i += 1
    return count