def binary_search(arr, n):
    low = 0
    high = n - 1

    if arr[0] == 0:
        return -1

    if arr[high] == 1:
        return high
    
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == 1 and arr[mid + 1] == 0:
            return mid

        elif arr[mid] == 0:
            high = mid - 1

        else:
            low = mid + 1

    return -1

def count_1s(arr):
    ans = binary_search(arr, len(arr))

    if ans == - 1:
        return 0
    
    else:
        return ans + 1
    
arr = [1,1,1,1,1,0,0,0]
print(count_1s(arr))