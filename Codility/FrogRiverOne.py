# A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0)
# and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
# You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
# The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only
# when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all
# the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly
# small, i.e. the leaves do not change their positions once they fall in the river.
#
# Write a function:
# def solution(X, A)
# that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.
# If the frog is never able to jump to the other side of the river, the function should return −1.
#Brute force: for each time value, check if all the positions are filled.
def solution(X, A):
    B = [0] * X
    S=0
    for i in range (0, len(A)):
        if (B[A[i]-1] == 0 and A[i]<=X): #First time we see a leaf falling
            S+=1
            B[A[i]-1] = 1
        if (S == X):
            return i
    return -1