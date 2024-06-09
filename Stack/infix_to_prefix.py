# Rules:
# 1. Reverse the expression
# 2. If we encounter an operand simply print it in the final ans
# 3. Bracket rule can be used same as in infix to postfix or opposite of it
# 4. Similar priority operator can stay together in the stack
# 5. Lowest priority operator cannot be placed on top of higher priority operator
#    -- if this happens then pop the top operator of stack and print it in the final ans and then push the current operator on the stack 
#    if the above conditions satisfy
# 6. At last return the reversed exp

def infix_to_prefix(exp):
    s = exp[::-1]
    d = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, ")": 0}
    stack = []
    res = ""

    for i in range(len(s)):
        if s[i] == ")":
            stack.append(s[i])

        elif s[i] == "(":
            while stack[-1] != ")":
                res = res + stack.pop()
            stack.pop()

        elif s[i] in d:
            while stack and d[stack[-1]] > d[s[i]]:
                res = res + stack.pop()
            stack.append(s[i])

        else:
            res += s[i]

    while stack:
        res += stack.pop()

    res = res[::-1]
    return res

exp = "k+l-m*n+(o^p)*w/u/v*t+q"
print(infix_to_prefix(exp))

