def binary_search(arr, n, x):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            high = mid - 1

        else:
            low = mid + 1

    return -1

arr = [1, 3, 5, 4, 9, 8, 10, 6, 2]
x = 5

print(binary_search(arr, len(arr), x))