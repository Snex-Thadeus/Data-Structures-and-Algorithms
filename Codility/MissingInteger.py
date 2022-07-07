# Write a function: def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.

def solution(A):
    A.sort()
    if A[len(A)-1] <= 0: #Last element
        return 1
    iso = False #IsOne
    for i in range(0, len(A)):
        if A[i] == 1:
            iso = True
    if iso == False:
        return 1
    for i in range(0, len(A)-1):
        if A[i] > 0 and (A[i+1]-A[i]) > 1:
            return A[i]+1 #The missing element
    return A[len(A)-1]+1 #Last element plus one #Missing number is at the end


A = [2, 3, 4, 6]
print(solution(A))