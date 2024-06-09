def replace_char(s, a, b):
    if len(s) == 0:
        return s
    
    smallOutput = replace_char(s[1:], a, b)
    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput
    
s = "abdhdaba"
print(replace_char(s, "a", "c"))