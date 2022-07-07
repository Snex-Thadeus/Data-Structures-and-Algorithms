# You are given an array A consisting of N integers.
# For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i].
# We say that these elements are non-divisors.
# For example, consider integer N = 5 and array A such that:
#
#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# For the following elements:
# A[0] = 3, the non-divisors are: 2, 6,
# A[1] = 1, the non-divisors are: 3, 2, 3, 6,
# A[2] = 2, the non-divisors are: 3, 3, 6,
# A[3] = 3, the non-divisors are: 2, 6,
# A[4] = 6, there aren't any non-divisors.
# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    MMax = max(A)
    counts = [0] * (1 + MMax)
    nnondiv = [0] * (1 + MMax)
    visited = [False] * (1 + MMax)
    for number in A:
        counts[number] += 1

    nondivisors = []
    for number in A:
        if visited[number]:
            nondivisors.append(nnondiv[number])
        else:
            nb_of_divisors = 0
            for divisor in range(1, int(number ** 0.5) + 1):
                if (number % divisor == 0):
                    nb_of_divisors += counts[divisor]
                    otherdiv = int(number / divisor)
                    if (otherdiv != divisor):
                        nb_of_divisors += counts[otherdiv]
            nondivisors.append(N - nb_of_divisors)
            nnondiv[number] = N - nb_of_divisors
            visited[number] = True
    return (nondivisors)



