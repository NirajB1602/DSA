def palindrome(s):
    n = len(s)
    if n == 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:n-1])
    return False

print(palindrome("racecar"))

# def palindrome(s, si, ei):
#     if si >= ei:
#         return True
#     if s[si] == s[ei]:
#         return palindrome(s, si+1, ei-1)
#     return False

# s = "wowow"
# print(palindrome(s, 0, len(s) - 1))