def is_scrambled(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if len(s1) == 0 and len(s2) == 0:
        return True

    if s1 == s2:
        return True
    
    if sorted(s1) != sorted(s2):
        return False
    
    n = len(s1)
    for i in range(1, n):
        if (is_scrambled(s1[:i], s2[:i]) and is_scrambled(s1[i:], s2[i:])):
            return True
        
        if (is_scrambled(s1[:i], s2[-i:]) and is_scrambled(s1[i:], s2[:-i])):
            return True
        
    return False    

s1 = "coder"
s2 = "ocred"
print(is_scrambled(s1, s2))
            

        
        

