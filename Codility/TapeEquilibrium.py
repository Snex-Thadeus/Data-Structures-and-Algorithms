# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
# For example, consider array A such that:
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:
# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:
# def solution(A)
# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
# Brute Solution: for p=1 to N, for i=0 to N,compute Sl and SR
#SR=S-SL  |SL - SR|=|SL-S+SL| = |2SL-S|

def solution(A):
    if len(A)<2:
        return 0
    s = sum(A)
    minDiff = 2000
    sL = 0
    for i in range(0, len(A)-1):
        sL+=A[i]
        diff = abs(2*sL-s)
        minDiff = min(minDiff, diff)

    return minDiff