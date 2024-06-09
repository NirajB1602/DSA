# Partition using Hoare's partition

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = hoare_partition(arr, low, high)
        quick_sort(arr, low, pivot_idx) # pivot is not guaranteed to return to its correct place after hoare's partition
        quick_sort(arr, pivot_idx + 1, high)

arr = [6, 3, 5, 1, 7, 9, 10, 8]
# print(hoare_partition(arr, 0, len(arr) - 1))

quick_sort(arr, 0, len(arr) - 1)
print(arr)

