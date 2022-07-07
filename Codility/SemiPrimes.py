# Write a function:
# def solution(N, P, Q)
# that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.
# For example, given an integer N = 26 and arrays P, Q such that:
#
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20
# the function should return the values [10, 4, 0], as explained above.

def solution(N, P, Q):
    primes = [1] * (N+1)
    primes[0]=primes[1]=0

    for i in range(2, int(N**0.5)+1):
        if primes[i]:
            k=i*i
            while k<N:
                primes[k]=0 #Not considered prime
                k+=i
    allsemiprimes = [0] * (N+1)
    for i in range(0, N+1):
        for j in range(0, N+1):
            if primes[i] and primes[j] and i*j<=N:
                allsemiprimes[i*j]=1
            if i*j > N:
                break
    semiprimes = [0] * len(P)
    semiprimescum = [0] * (N+1)
    s=0

    for i in range(0, N+1):
        s+=allsemiprimes[i]
        semiprimescum[i]=s

    for i in range(0, len(P)):
        semiprimes[i]=semiprimescum[Q[i]] - semiprimescum[P[i]-1]
    return semiprimes