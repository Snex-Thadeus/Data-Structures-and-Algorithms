# A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.
# The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:
# 0 represents a position without a leaf;
# 1 represents a position containing a leaf.
# The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.
#
# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

def fibN(N):
    fib = [0] * 100
    fib[1] = 1
    for i in range(2, 100):
        fib[i] = fib[i-1] + fib[i - 2]
        if fib[i] > N:
            return fib[2:i] #Slashed the first 2 elements that are not needed


def solution(A):
    A.append(1)
    fib = fibN(len(A))
    reachsteps = [0] * (len(A))

    # leafs that can be reached in one step first
    for j in fib:
        if A[j-1] == 1:
            reachsteps[j-1] = 1
    # searcg leafs with more than one step
    for i in range(len(A)):
        if A[i] == 0 or reachsteps[i] > 0:
            continue #No leafs

        min_i = -1
        min_v = 100000
        for j in fib:
            previousi = i - j
            if previousi < 0:
                break
            if reachsteps[previousi] > 0 and min_v > reachsteps[previousi]:
                min_v = reachsteps[previousi]
                min_i = previousi
        if min_i != -1:
            reachsteps[i] = min_v+1
    if reachsteps[len(A)-1] > 0:
        return reachsteps[len(A)-1]
    else:
        return -1
