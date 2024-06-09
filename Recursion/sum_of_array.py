def sum_of_array(arr):
    n = len(arr)
    if n == 0:
        return 0
    output = sum_of_array(arr[:n-1])
    return arr[n-1] + output

arr = [5, 4, 2, 10, 4]
print(sum_of_array(arr))