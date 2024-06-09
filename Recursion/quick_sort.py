def partition(lst, si, ei):
    pivot = lst[si]
    cnt = 0
    for i in range(si, ei + 1):
        if lst[i] < pivot:
            cnt += 1

    pivot_index = si + cnt
    lst[si], lst[pivot_index] = lst[pivot_index], lst[si]

    i = si
    j = ei
    while i < j:
        if lst[i] < pivot:
            i += 1
        elif lst[j] >= pivot:
            j -= 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
            j -= 1
            i += 1

    return pivot_index

def quick_sort(lst, si, ei):
    if si >= ei:
        return
    
    pivot_index = partition(lst, si, ei)
    quick_sort(lst, si, pivot_index - 1)
    quick_sort(lst, pivot_index + 1, ei)

    return lst

lst = [7, 8, 4, 1, 2, 5, 9, 10]
print(quick_sort(lst, 0, len(lst) - 1))