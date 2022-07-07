# An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
# For example, consider array A such that
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
# Write a function
# def solution(A)
# that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs.
# The function should return −1 if array A does not have a dominator.

def solution(A):
    if len(A)==0:
        return 1
    if len(A)==1:
        return 0
    B=A.copy() #B = sorted(A)
    B.sort()

    c=1 #Number of occurrences
    n=len(B)
    for i in range(1,n):
        if B[i] != B[i-1]:
            c=1
        else:
            c+=1
        if c>int(n/2):
            return A.index(B[i])

    return -1


def solution(A):
    D = {}
    d = len(A) / 2
    for i, v in enumerate(A): #Python's enumerate() lets you write Pythonic for loops when you need a count and the value from an iterable.
        if v in D:
            D[v] += 1
        else:
            D[v] = 1
        if D[v] > d:
            return i
    return -1