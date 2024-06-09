def remove_duplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s
    smallOutput = remove_duplicates(s[1:])
    if s[0] == s[1]:
        return smallOutput
    else:
        return s[0] + smallOutput
    
s = "xxyyyzzxyxxzz"
print(remove_duplicates(s))
    
