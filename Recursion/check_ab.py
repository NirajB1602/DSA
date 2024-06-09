# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'

def check_ab(s):
    if len(s) == 0:
        return True
    if s[0] == "a":
        if len(s[1:]) > 0 and s[1:3] == "bb":
            return check_ab(s[3:])
        else:
            return check_ab(s[1:])
    return False

print(check_ab("abbab"))