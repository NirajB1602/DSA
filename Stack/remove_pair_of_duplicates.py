def removePair(s):
    stack = []
    cnt = 0
    output = ""
    
    for i in s:
        if cnt == 0 or i != stack[-1]:
            stack.append(i)
            cnt += 1
            
        else:
            stack.pop()
            cnt -= 1
            
    if cnt == 0:
        return "Empty String"

    while cnt:
        output = stack.pop() + output
        cnt -= 1
        
    return output

s = "abba"
print(removePair(s))