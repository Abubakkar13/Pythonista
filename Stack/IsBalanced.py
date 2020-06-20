"""
Given a string expression, check if brackets present in the expression are balanced or not. Brackets are balanced if the bracket which opens last, closes first.
You need to return true if it is balanced, false otherwise.

Sample Input 1 :
{ a + [ b+ (c + d)] + (e + f) }
Sample Output 1 :
true

Sample Input 2 :
{ a + [ b - c } ]
Sample Output 2 :
false


"""



def Pairs(open,close):
    # know they are in pair
    if open =='[' and close ==']':
        return True
    if open =='{' and close =='}':
        return True
    if open =='(' and close ==')':
        return True
    return False

def isBalanced(A):
    stack = []
    for i in range(len(A)):
        # check for opening square brackets and append it
        if A[i] =="[" or A[i] =='(' or A[i] =='{':
            stack.append(A[i])
        elif A[i] ==']' or A[i] ==')' or A[i] =="}":
            if Pairs(stack[-1],A[i]) or len(stack) != 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False
A="[(){]"
print(isBalanced(A))



