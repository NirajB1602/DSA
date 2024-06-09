def floor_element(arr, x):
    n = len(arr)

    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= x and (mid == n - 1 or arr[mid + 1] > x):
            return mid
        
        elif arr[mid] > x:
            high = mid - 1

        else:
            low = mid + 1

    return -1

arr = [1,2,8,10,11,12,19]
x = 20

print(floor_element(arr, x))