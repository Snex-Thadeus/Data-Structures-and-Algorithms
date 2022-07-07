# A non-empty array A consisting of N integers is given.
# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.
# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].
# For example, array A such that:
#
#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# contains the following example double slices:
# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.
# Write a function:
#
# def solution(A)
# that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

def solution(A):
    n=len(A)
    if n<=3:
        return 0
    LR = n*[0]
    RL = n*[0]

    s=0
    for i in range(1, n-1): #Discarding the edges
        s+=A[i]
        if s<0:
            s=0
        LR[i]=s

    s=0
    for i in range(n-2, 0, -1): #n-2 = is the highest edge
        s+=A[i]
        if s<0:
            s=0
        RL[i]=s

    m=0 #Max sum
    for i in range(0, n-2):
        m=max(m, LR[i]+RL[i+2]) #Skipping i+1

    return m