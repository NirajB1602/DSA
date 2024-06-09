def replace_pi(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    smallOutput = replace_pi(s[1:])
    if s[0] == "p" and s[1] == "i":
        return "3.14" + smallOutput[1:]
    else:
        return s[0] + smallOutput
    
s = "abpidabpia"
print(replace_pi(s))