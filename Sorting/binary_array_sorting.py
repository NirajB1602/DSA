def binary_array_Sort(arr, n): 
    i = 0
    j = n - 1
        
    while True:
        while i < n and arr[i] == 0:
            i += 1
                
        while j >=0 and arr[j] == 1:
            j -= 1
                
        if i >= j:
           break
            
        arr[i], arr[j] = arr[j], arr[i]

arr = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
binary_array_Sort(arr, len(arr))
print(arr)