def bubble_sort(arr, n):
    for i in range(n-1):
        swapped = False
        for j in range(1, n-i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        
        if swapped == False:
            break

arr = [2, 3, 5, 4, 9, 8, 6, 7, 10, 1]
bubble_sort(arr, len(arr))
print(arr)
