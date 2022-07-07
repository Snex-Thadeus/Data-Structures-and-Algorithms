def solution(A, K):
    if len(A) == 0:
        return A
    K = K%len(A)
    return A[-K:] + A[:-K]

# A is an array while K is the number the array A is to be rotated #Codility test
# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index,
# and the last element of the array is moved to the first place.

A = [3, 8, 9, 7, 6, 5]
K = 3

result = solution(A, K)
print(result)