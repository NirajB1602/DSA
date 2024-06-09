def merge(arr, low, mid, high):
    left = arr[low : mid+1]
    right = arr[mid+1 : high]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1

        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        merge(arr, low, mid, high)

arr = [10, 15, 20, 40, 8, 11, 55]
merge_sort(arr, 0, len(arr) - 1)
print(arr)

