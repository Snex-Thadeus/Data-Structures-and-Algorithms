# Write a function:
# def solution(S, P, Q)
# that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers,
# returns an array consisting of M integers specifying the consecutive answers to all queries.
# Result array should be returned as an array of integers.
# For example, given the string S = CAGCCTA and arrays P, Q such that:
#
#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6
# the function should return the values [2, 4, 1], as explained above.

def solution(S, P, Q):
    R=[] #Empty list R for the result
    A=[0]*len(S) #Initialised at zero with a len(S)
    C=[0]*len(S)
    G=[0]*len(S)
    T=[0]*len(S)

    a=c=g=t=0 #Counters

    for i in range(0, len(S)):
        if S[i]=='A':
            a+=1
        elif S[i]=='C':
            c+=1
        elif S[i]=='G':
            g+=1
        elif S[i]=='T':
            t+=1

        A[i]=a
        C[i]=c
        G[i]=g
        T[i]=t

    for i in range(0, len(P)):
        if P[i]==G[i]:
            if S[P[i]]=='A':
                R.append(1)
            elif S[P[i]]=='C':
                R.append(2)
            elif S[P[i]]=='G':
                R.append(3)
            elif S[P[i]]=='T':
                R.append(4)

        elif A[P[i]]<A[Q[i]] or S[P[i]]=='A':
            R.append(1)
        elif C[P[i]]<C[Q[i]] or S[P[i]]=='C':
            R.append(2)
        elif G[P[i]]<G[Q[i]] or S[P[i]]=='G':
            R.append(3)
        elif T[P[i]]<T[Q[i]] or S[P[i]]=='T':
            R.append(4)

    return R

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is
# paired together, and then the second item in each passed iterator are paired together etc.

# This is the right code that gives 100%

def solution(S, P, Q):
    # write your code in Python 3.6
    ans = []
    for (p, q) in zip(P, Q):
        if 'A' in S[p:q + 1]:
            ans.append(1)
        elif 'C' in S[p:q + 1]:
            ans.append(2)
        elif 'G' in S[p:q + 1]:
            ans.append(3)
        else:
            ans.append(4)

    return ans