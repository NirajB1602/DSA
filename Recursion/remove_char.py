def remove_char(s, char):
    if len(s) == 0:
        return ""
    
    smallOutput = remove_char(s[1:], char)
    if s[0] == char:
        return smallOutput
    else:
        return s[0] + smallOutput
    
s = "abbxc"
print(remove_char(s, "b"))


    
