# A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.
#
# A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.
#
# You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.
# For example, given:
# N = 15 and M = 75, the prime divisors are the same: {3, 5};
# N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
# N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
# Write a function:
# def solution(A, B)
# that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)


def solution(A, B):
    l = len(A)
    cnt=0
    for i in range(0,l):
        a=A[i]
        b=B[i]
        D=gcd(a,b)
        while (gcd(a,D) !=1):
            a/=gcd(a,D)
        while (gcd(b,D) !=1):
            b/=gcd(b,D)
        if(a==1 and b==1):
            cnt+=1
    return cnt