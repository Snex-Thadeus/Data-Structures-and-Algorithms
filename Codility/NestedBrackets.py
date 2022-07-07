# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
# Write a function:
# def solution(S)
# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

def solution(S):
    if (len(S)==0):
        return 1
    V =[]
    c = {'[':+1, ']':-1, '(':+2, ')':-2, '{':3, '}':-3}
    for i in range(0, len(S)):
        if(i==0 and c[S[i]]<0): #]()[] Closing character
            return 0
        if (c[S[i]]<0 and len(V)==0): #() )
            return 0
        if (c[S[i]]<0 and c[S[i]] !=-V[-1]): #{ (] last positive/opening character
            return 0
        elif (c[S[i]]<0): #Last negative index
            V.pop() #Pop the last element
        else:
            V.append(c[S[i]])  # Append the new element with a positive index

    if(len(V)==0): #WE have properly closed all the previously opened characters
        return 1
    else:
        return 0



def solution(S):
    n = len(S)
    s = []
    for k in S:
        if k in "([{":
            s.append(k)
        else:
            if len(s) == 0:
                return 0
            if k == ')' and s[-1] == '(':
                s.pop()
            if k == ']' and s[-1] == '[':
                s.pop()
            if k == '}' and s[-1] == '{':
                s.pop()
    if len(s) == 0:
        return 1
    else:
        return 0

