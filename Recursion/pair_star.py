def pair_star(s):
    if len(s) == 1:
        return s
    if s[0] == s[1]:
        return s[0] + "*" + pair_star(s[1:])
    else:
        return s[0] + pair_star(s[1:])
    
s = "hello"
print(pair_star(s))