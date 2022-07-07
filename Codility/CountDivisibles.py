# Write a function:
# def solution(A, B, K)
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
# { i : A ≤ i ≤ B, i mod K = 0 }
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2
# within the range [6..11], namely 6, 8 and 10.
#Brute: for each number between A & B, if number is divible by K, increment counter. return counter

def solution(A, B, K):
    c=int(B/K) - int(A/K) #Counterof divisibles b2n 0 and B
    if (A%K==0):
        c=c+1
    return c

A = 4
B = 20
K = 5
print(solution(A,B,K))