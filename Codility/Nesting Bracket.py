# A string S consisting of N characters is called properly nested if:
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
# Write a function:
# def solution(S)
# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

def solution(S):
    p=0
    for i in range(0, len(S)):
        if S[i]=='(':
            p+=1
        elif S[i]==')':
            p-=1
        if p<0: #Inbalanced parenthesis
            return 0
    if p!=0: #Different number of opening and closing parenthesis
        return 0
    else:
        return 1