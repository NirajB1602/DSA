# def convert_str_to_int(s):
#     if len(s) == 0:
#         return 0
#     if s[0] == 0:
#         return convert_str_to_int(s[1:])
#     else:
#         return int(s[0]) * (10 ** len(s[1:])) + convert_str_to_int(s[1:])
    
# print(convert_str_to_int("012"))

def convert_str_to_int(s):
    if len(s) == 0:
        return 0
    si = 0
    if s[si] == 0:
        return convert_str_to_int(s[si+1:])
    else:
        return int(s[si]) * (10 ** len(s[si+1:])) + convert_str_to_int(s[si+1:])
    
print(convert_str_to_int("123456789"))