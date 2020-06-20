def postfix_expression(arr):
    stack = []
    operator = ["+","-","/","*","%"]

    for item in arr:
        if item not in operator: # it is an operand
            stack.append(item) # push into the stack
        else:
            first = int(stack.pop())
            second = int(stack.pop())
        if (item == "+"):
            stack.append(second + first)

        if (item == "-"):
            stack.append(second - first)

        if (item == "*"):
            stack.append(second * first)

        if (item == "/"):
            stack.append(second / first)

        if (item == "%"):
            stack.append(second % first)
# return last value of the stack
    return stack[-1]
A = ["2" , "1", "+", "3", "*"]
print(postfix_expression(A))
