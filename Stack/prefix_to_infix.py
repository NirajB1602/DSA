# Rules:
# 1. Reverse the expression
# 2. If we encounter any operand then simply push it on the stack
# 3. If we encounter an operator then pop the top two elements of the stack and add operator in between them 
#     -- (keep in mind first place the top operand then operator and then the second last operand)
#     -- after this is done then place that expression on the stack

def postfix_to_infix(exp):
    s = exp[::-1]
    stack = []
    
    for i in range(len(s)):
        if s[i].isalpha():
            stack.append(s[i])

        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            # small_exp = operand1 + exp[i] + operand2
            small_exp = "(" + operand1 + s[i] + operand2 + ")"
            stack.append(small_exp)

    return stack.pop()

exp = "*+ab/ef"
print(postfix_to_infix(exp))