def peak_element(arr):
    n = len(arr)
    if n == 1 or arr[0] > arr[1]:
        return 0
        
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    
    low = 0
    high = n - 1
    
    while low <= high:
        mid = low + (high - low) // 2
    
        if (arr[mid] >= arr[mid-1]) and (arr[mid] >= arr[mid+1]):
            return mid
            
        elif arr[mid] < arr[mid + 1]:
            low = mid + 1
                
        else:
            high = mid - 1
    
    return -1

arr = [1, 2, 3, 4, 5, 2, 1]
print(peak_element(arr))