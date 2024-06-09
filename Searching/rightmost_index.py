def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    if arr[high] == x:
        return high
    
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x:
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

        elif arr[mid] == x and (mid == len(arr) - 1 or arr[mid + 1] != x):
            return mid
        
        else:
            low = mid + 1

    return -1

arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7]
x = 0

print(binary_search(arr, x))