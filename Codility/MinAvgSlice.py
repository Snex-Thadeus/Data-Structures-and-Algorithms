# Write a function:
# def solution(A)
# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal
# average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.
#
# The goal is to find the starting position of a slice whose average is minimal

def solution(A):
    mn=max(A)*2 #Minimum
    mi = 0 #Index
    for i in range(0, len(A)-2):
        v1 = (A[i]+A[i+1]+A[i+2])/3
        v2 = (A[i]+A[i+1])/2
        if mn>v1 or mn>v2:
            mn=min(v1,v2)
            mi=i
    if mn > (A[-1]+A[-2])/2: #Last 2 elements
        return len(A)-2

    return mi