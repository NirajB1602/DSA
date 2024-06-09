# Partition using Lomuto partition

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = lomuto_partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1) # pivot is guaranteed to return to its correct place after lomuto partition
        quick_sort(arr, pivot_idx + 1, high)

arr = [2, 3, 5, 1, 7, 9, 10, 6, 2, 8]
# print(lomuto_partition(arr, 0, len(arr) - 1))

quick_sort(arr, 0, len(arr) - 1)
print(arr)