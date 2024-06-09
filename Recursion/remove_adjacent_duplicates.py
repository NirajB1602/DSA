def remove_adjacent_duplicates(s, si, ei):
    if si == ei:
        return s[si]
    
    if si > ei:
        return ""
    
    if s[si] == s[si + 1]:
        while si < ei and s[si] == s[si + 1]:
            si += 1
        return remove_adjacent_duplicates(s, si+1, ei)
        
    else:
        return s[si] + remove_adjacent_duplicates(s, si+1, ei)
    
# recursively remove all duplicates
# azxxzy = azzy = ay

def recursively_remove_adjacent_duplicates(s):
    new_str = ""
    while s != new_str:
        new_str = s
        s = remove_adjacent_duplicates(s, 0, len(s) - 1)

    return s


s = "azxxxzya"
# print(remove_adjacent_duplicates(s, 0, len(s) - 1))
print(recursively_remove_adjacent_duplicates(remove_adjacent_duplicates(s, 0, len(s) - 1)))