def merge(l1, l2, lst):
    i = 0
    j = 0
    k = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lst[k] = l1[i]
            k += 1
            i += 1 
        else:
            lst[k] = l2[j]
            k += 1
            j += 1 

    while i < len(l1):
        lst[k] = l1[i]
        k += 1
        i += 1 

    while j < len(l2):
        lst[k] = l2[j]
        k += 1
        j += 1 
    
    return lst

def merge_sort(lst):
    n = len(lst) 
    if n == 0 or n == 1:
        return
    
    mid = n//2
    l1 = lst[:mid]
    l2 = lst[mid:]

    merge_sort(l1)
    merge_sort(l2)

    return merge(l1, l2, lst)

print(merge_sort([1, 2, 4, 3, 8, 5, 2, 4, 6]))

