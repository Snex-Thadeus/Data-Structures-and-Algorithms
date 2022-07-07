# Write a function:
# def solution(H)
# that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.
# For example, given array H containing N = 9 integers:
#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.

def solution(H):
    last=0
    c=0 #Counter of the number os stones
    S=[]
    for i in range(0, len(H)):
        if(H[i]>last): #Higher than the previous level
            last=H[i]
            c+=1 #Increase stones
            S.append(H[i])
        elif(H[i]<last): #Lower than the previous level
            while(len(S)>0 and H[i]<S[-1]): #S[-1]=Highest level contained in S
                S.pop()
            if(len(S)==0 or H[i] !=S[-1]):
                c+=1
                S.append(H[i])
            last=H[i]
    return c