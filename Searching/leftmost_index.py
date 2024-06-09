def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    if arr[0] == x:
        return 0

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x:
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

        elif arr[mid] == x and (mid == 0 or arr[mid - 1] != x):
            return mid
        
        else:
            high = mid - 1

    return -1

arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]
x = 5

print(binary_search(arr, x))