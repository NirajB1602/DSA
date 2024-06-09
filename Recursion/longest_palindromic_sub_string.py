def maxi(a, b):
    return a if a > b else b

def longest_palindromic_substring(s, si, ei, cnt = 0):
    if si > ei:
        return cnt
    
    if si == ei:
        return cnt + 1
    
    if s[si] == s[ei]:
        count1 = longest_palindromic_substring(s, si+1, ei-1, cnt + 2)
        count2 = longest_palindromic_substring(s, si+1, ei, 0)
        count3 = longest_palindromic_substring(s, si, ei-1, 0)
        return maxi(count1, maxi(count2, count3))       
    
    else:
        res1 = longest_palindromic_substring(s, si+1, ei, 0)
        res2 = longest_palindromic_substring(s, si, ei-1, 0)
        return maxi(res1, res2)
        

s = "aaaabbaa"
print(longest_palindromic_substring(s, 0, len(s) - 1))
