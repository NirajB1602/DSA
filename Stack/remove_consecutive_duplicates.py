def removeConsecutiveDuplicates(s):
    res = ""
    stack = []
    
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
            
    for i in stack:
        res += i
        
    return res

s = "aaaaaaaaaaabbbbbbbbbbbbbbccccccccccaaaaaaaannn"
print(removeConsecutiveDuplicates(s))