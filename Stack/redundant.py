"""
Given a string mathematical expression, return true if redundant brackets are present in the expression. Brackets are redundant if there is nothing inside the bracket or more than one pair of brackets are present.
Assume the given string expression is balanced and contains only one type of bracket i.e. ().

Sample Input 1:
((a + b))
Sample Output 1:
true
Sample Input 2:
(a+b)
Sample Output 2:
false

"""

def redundant_brackets(N):
    stack = []
    for i in range(len(N)):
        if N[i] in ('(+*/'):
            stack.append(N[i])
        elif N[i] == ')':
             if stack.pop() =='(':
                 return 1 # 1  is for Redudant
             stack.pop()
    return 0 # Non redundat

N ="((a+b))"
a = redundant_brackets(N)
if a == 1:
    print("It is redundant")
else:
    print("Non redundat")
