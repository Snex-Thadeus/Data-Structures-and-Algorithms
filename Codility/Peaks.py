# A non-empty array A consisting of N integers is given.
# A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that
# 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].
# Write a function:
# def solution(A)
# that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.
# If A cannot be divided into some number of blocks, the function should return 0.
#
# For example, given:
#
#     A[0] = 1
#     A[1] = 2
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# the function should return 3, as explained above.

def solution(A):
    P = []  # Picks
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            P.append(i)  # Append the index/pick of the current position to picks

    if len(P) == 0:
        return 0

    for k in range(len(P), 0, -1):
        if len(A)%k !=0: #Can't divide A into equal slices
            continue

        lenslice = len(A)//k
        slices = [0]*k #Slices list equal to size k
        ss = 0 #sum of pick

        for ip in P:
            slice_id = ip//lenslice
            if slices[slice_id] == 0: #No picks found for slice_id
                slices[slice_id] = 1
                ss +=1
        if ss == k:
            return k

    return 0
























