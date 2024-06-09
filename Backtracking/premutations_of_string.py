def print_permutations(lst):
    for i in lst:
        print(i, end="")
    print()

def find_permutations(lst, idx=0):
    if idx >= len(lst):
        print_permutations(lst)
        return

    for i in range(idx, len(lst)):
        lst[i], lst[idx] = lst[idx], lst[i]
        find_permutations(lst, idx + 1)
        lst[i], lst[idx] = lst[idx], lst[i]
    
s = "ABB"
find_permutations(list(s))

