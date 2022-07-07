# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both
# ends in the binary representation of N.
# Read the sequence
# Increment a counter variable for each digit
# Reset my counter every time I reach a "1" digit
# 100010001
# Exceptions: 100100010000 & 000010010001
def solution(N):
    N=bin(N)[2:] #Convert N into a binary and skip the first 2 numbers which are 0 and B
    b=0 #counter
    maxb = 0
    for k in N:
        if int(k) == 0:
            b+=1
        elif int(k) == 1:
            maxb = max(b, maxb)
            b=0
    return maxb


