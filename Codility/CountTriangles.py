# An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:
#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 12
# There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).
# Write a function:
# def solution(A)
# that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

def solution(A):
    A.sort()  # sort the array so that we can only check only whether x+y>z among all other triangle inequalities where x<y<z.
    lenA = len(A)

    res = 0
    for x in range(lenA - 2):
        z = x + 2
        for y in range(x + 1, lenA - 1):
            # A[y]-A[x] is always smaller than A[z] since A[x] and A[y] is already smaller than A[z] in this sorted array.
            # only check for the sum(if x+y>z then z-y>x, z-x>y)
            # x-y<z since x,y<z in a sorted array.
            # if z>x,y; then x+z>y and y+z>x. Only need to check whether x+y>z
            total = A[x] + A[y]
            # increment z which will be valid for the next y values as well since if curr total>A[z];
            # then next totals will definetely be.
            while z < lenA and total > A[z]:
                z += 1
            res += (
                               z - 1) - y  # decrement 1 since this z position is the next position we will check; z-1 is the last valid position.
    return res