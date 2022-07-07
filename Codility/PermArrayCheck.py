# A non-empty array A consisting of N integers is given.
# A permutation is a sequence containing each element from 1 to N once, and only once.
# Write a function:
# def solution(A)
# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
# Brute Force: for each number 1 to N, test if it's in the Array && scan the whole array
# to test if the occurrence is only once = High complexity solution
def solution(A):
    if len(A)==0:
        return 0
    A.sort()
    for i in range(0,len(A)):
        if A[i] != (i+1):
            return 0
    return 1