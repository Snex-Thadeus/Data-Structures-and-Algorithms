# Write a function:
# def solution(K, A)
# that, given an integer K and a non-empty array A of N integers, returns the maximum number of ropes of length greater than or equal to K that can be created.

# in the example, one case is missing: rope 3.
# so rope1 and 2, 3 and 4,5 are three such ropes.
def solution(K, A):
    length = 0
    res = 0
    for a in A:
        length += a
        if length >= K:
            res += 1
            length = 0

    return res