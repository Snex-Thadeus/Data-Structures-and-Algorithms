# Write a function
# def solution(A)
# that, given an array A consisting of N integers, returns the number of distinct values in array A.

def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    c=1
    for i in range(1, len(A)):
        if A[i]!=A[i-1]:
            c+=1
    return c


def sol(A):
    A=set(A)
    return(len(A))