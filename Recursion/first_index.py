def first_index(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if x == arr[0]:
        return 0
    res = first_index(arr[1:], x)
    if res == -1:
        return -1
    else:
        return res+1

arr = [10, 6, 9, 4, 8]
print(first_index(arr, 8))