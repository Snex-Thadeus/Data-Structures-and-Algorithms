# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index,
# and the last element of the array is moved to the first place.
# For example, given
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]
def solution(A, K):
    N = len(A)
    #B=.copy()
    B = [None] * N #Empty Vector
    for i in range(0, N):
        B[(i+K)%N] = A[i]
    return B