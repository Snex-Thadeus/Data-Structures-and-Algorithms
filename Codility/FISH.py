# Write a function:
# def solution(A, B)
# that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.
#
# For example, consider arrays A and B such that:
#
#   A[0] = 4    B[0] = 0
#   A[1] = 3    B[1] = 1
#   A[2] = 2    B[2] = 0
#   A[3] = 1    B[3] = 0
#   A[4] = 5    B[4] = 0
# Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2
# and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it.
# The remaining two fish, number 0 and 4, never meet and therefore stay alive.

def solution(A, B):
    ds = [] #Downstreamlist
    c=0 #Counter of eaten fish
    for i in range(0, len(B)):
        if (B[i]==1): #Going downstream
            ds.append(A[i])
        else:
            while(len(ds) !=0): #Test if the size of the last downstream fish > the size of the upstream fish
                if(ds[-1]>A[i]):
                    c=c+1
                    break
                elif ds[-1]<A[i]: #Downstream fish is of smaller size than upstream
                    ds.pop() #Ut has been eaten
                    c=c+1
    return len(A)-c

