def check_num(arr, x):
    n = len(arr)
    if n == 0:
        return False
    
    if x == arr[n-1]:
        return True
    return check_num(arr[:n-1], x)

arr = [1, 2, 4, 6, 8, 9, 10]
print(check_num(arr, 11))
