# def last_index(arr, x):
#     n = len(arr)
#     if n == 0:
#         return -1
#     if x == arr[n-1]:
#         return n-1
#     return last_index(arr[:n-1], x)


def last_index(arr, x, si):
    n = len(arr)
    if si == n:
        return -1
    smallerlistoutput = last_index(arr, x, si+1)
    if smallerlistoutput != -1:
        return smallerlistoutput
    else:
        if arr[si] == x:
            return si
        else:
            return -1
        
arr = [10, 4, 8, 6, 9, 4, 8]
print(last_index(arr, 4, 0))