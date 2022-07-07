# Write a function:
# def solution(A)
# that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.
# For example, the following array A:
#
#     A[0] = 1
#     A[1] = 5
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
    if(len(A)<3):
        return 0
    P=[] #Picks
    for i in range(1, len(A)-1):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            P.append(i) #Append the index/pick of the current position to picks

    if len(P)==0:
        return 0
    elif len(P)==1:
        return 1

    c=1
    m=0

    for k in range(min(len(P), int(len(A)**0.5))+1, 0, -1):
        lastF=0 #Index of last flag/pick
        c=1 #One flag
        for i in range(1, len(P)):
            if (P[i]-P[lastF]) >= k and c<k:
                c+=1
                lastF=i

        if c<m:
            return m #Maximum
        elif m<c:
            m=c

