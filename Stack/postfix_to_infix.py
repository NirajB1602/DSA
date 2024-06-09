# Rules:
# 1. If we encounter any operand then simply push it on the stack
# 2. If we encounter an operator then pop the top two elements of the stack and add operator in between them 
#     -- (keep in mind first place the second last operand then operator and then the top operand)
#     -- after this is done then place that expression on the stack

def postfix_to_infix(exp):
    stack = []
    
    for i in range(len(exp)):
        if exp[i].isalpha():
            stack.append(exp[i])

        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            # small_exp = operand2 + exp[i] + operand1
            small_exp = "(" + operand2 + exp[i] + operand1 + ")"
            stack.append(small_exp)

    return stack.pop()

exp = "ab+ef/*"
print(postfix_to_infix(exp))