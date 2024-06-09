def selection_sort(arr, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [10, 5, 8, 20, 2, 18]
selection_sort(arr, len(arr))
print(arr)
   
            