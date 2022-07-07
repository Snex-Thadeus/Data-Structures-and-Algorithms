# A non-empty array A consisting of N integers is given.
# The leader of this array is the value that occurs in more than half of the elements of A.
# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
# Write a function:
# def solution(A)
# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

def solution(A):
    B=A.copy()
    B.sort()
    c=1 #Counter of occurrences
    l=0 #Holds value of the leader
    n=0 #Count of the total occurrences of the leader value

    for i in range(1, len(B)): #Find value of the leader
        if (B[i] != B[i-1]):
            c=1
        else:
            c+=1
        if c>len(B)/2:
            l=B[i]
            break
    for i in range(0, len(A)): #Count number of occurrences of the leader value in A
        if A[i]==l:
            n+=1

    EqL=0
    c=0
    for i in range(0, len(A)):
        if A[i]==l:
            c+=1 #Number of the occurrence of the leader value on the left
        if (i+1<2*c and len(A)-i-1<2*(n-c)): #Right side
            EqL+=1

    return EqL
