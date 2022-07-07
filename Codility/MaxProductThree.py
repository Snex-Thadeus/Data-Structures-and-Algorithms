# A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to
# A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
#
# Write a function:
# def solution(A)
# that, given a non-empty array A, returns the value of the maximal product of any triplet.

def solution(A):
    A.sort()
    N=len(A)
    P1 = A[N-1]*A[0]*A[1] #Product of the first 2 and the last
    P2 = A[N-1]*A[N-2]*A[N-3] #Product of the last 3
    return max(P1,P2)