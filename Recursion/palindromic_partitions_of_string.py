def isPalindrome(s, si, ei):
    if len(s) <= 1:
        return True
    while si < ei: 
        if s[si] == s[ei]:
            return isPalindrome(s, si+1, ei - 1)
        else:
            return False
        
    return True
    
def partitions(s, idx, temp=[], sol=[]):
    if idx == len(s):
        sol.append(list(temp))
        return 
    
    char = ""
    for i in range(idx, len(s)):
        char += s[i]
        if isPalindrome(char, 0, len(char) - 1):
            temp.append(char)
            partitions(s, idx+1, temp, sol)
            temp.pop()

    return sol

s = "geeks"
print(partitions(s, 0))
    
