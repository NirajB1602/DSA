# Rules:
# 1. If we encounter an operand then simply print it in the final ans
# 2. No 2 operators of same priority can stay together in the stack
#    -- if this happens then pop the top operator of stack and print it in the final ans and then push the current operator on the stack
# 3. Lowest priority operator cannot be placed on top of higher priority operator
#    -- if this happens then pop the top operator of stack and print it in the final ans and then push the current operator on the stack 
#    if the above conditions satisfy

def InfixtoPostfix(exp):
    d = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0}
    res = ""
    stack = []

    for i in range(len(exp)):
        if exp[i] == "(":
            stack.append(exp[i])

        elif exp[i] == ")":
            while stack[-1] != "(":
                res = res + stack.pop()
            stack.pop()

        elif exp[i] in d:
            while stack and d[stack[-1]] >= d[exp[i]]:
                res = res + stack.pop()
            stack.append(exp[i])

        else:
            res = res + exp[i]

    while stack:
        res = res + stack.pop()

    return res


exp = "a+b/c-d*a"
print(InfixtoPostfix(exp))
