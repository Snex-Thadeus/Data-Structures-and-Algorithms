# You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:
#
# with your first step you can stand on rung 1 or 2,
# if you are on rung K, you can move to rungs K + 1 or K + 2,
# finally you have to stand on rung N.
# Your task is to count the number of different ways of climbing to the top of the ladder.
#
# Write a function:
# def solution(A, B)
# that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].


def solution(A, B):
    # write your code in Python 3.6
    maxFibNum = max(A)
    fib = [0] * (maxFibNum + 1)

    # precompute fibonacci numbers until max fib
    fib[0] = fib[1] = 1
    for i in range(2, maxFibNum + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    res = []
    for a, b in zip(A, B):
        res += [fib[a] & (2 ** b - 1)]  # fib[a]%(2**b)

    return res