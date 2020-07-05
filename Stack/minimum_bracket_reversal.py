"""
Minimum bracket Reversal
Send Feedback
Given a string expression which consists only ‘}’ and ‘{‘. The expression may not be balanced. You need to find the minimum number of bracket reversals which are required to make the expression balanced.
Return -1 if the given expression can't be balanced.
Input Format :
String S
Output Format :
Required count
Sample Input 1 :
{{{
Sample Output 1 :
-1
Sample Input 2 :
{{{{}}
Sample Output 2 :
1

"""






def minimum_reversal(string):
    if len(string) == 0:
        return 0
    if len(string) % 2 !=0:
        return -1
    stack = []
    for item in string:
        if item =='{':
            stack.append(item)
        else:
            if (len(stack) !=0 and stack[-1] =="{"):
                stack.pop()
            else:
                stack.append(item)
    count = 0
    while (len(stack )!= 0):
        c1 = stack.pop()
        c2 = stack.pop()
        if c1 != c2:
            count += 2
        else:
            count += 1
    return count
string = input("Enter the string : ")
answer = minimum_reversal(string)
print(answer)