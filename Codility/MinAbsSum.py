# For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:
# val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
# (Assume that the sum of zero elements equals zero.)
# For a given array A, we are looking for such a sequence S that minimizes val(A,S).
# Write a function:
# def solution(A)
# that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

#DYNAMIC PROGRAMMING
import math


def solution(A):
    if A == []:
        return 0
    A = list(map(abs, A))
    maxElem = max(A)
    total = sum(A)

    count = [0] * (maxElem + 1)
    for a in A:
        count[a] += 1

    dp = [-1] * (total + 1)  # -1 means this sum is not reached.
    # otherwise, this sum is reached

    dp[0] = 0  # if we only have 1 elem, this makes it equal to that elem
    for j in range(1, maxElem + 1):
        if count[j] > 0:
            for i in range(total + 1):
                if dp[i] >= 0:
                    dp[i] = count[j]
                elif i >= j and dp[i - j] >= 0:
                    dp[i] = dp[i - j] - 1

    res = math.inf
    for i in range(total // 2 + 1):
        if dp[i] >= 0:
            res = min(res, total - 2 * i)  # (total-i)-i, the diff of two parts

    return res