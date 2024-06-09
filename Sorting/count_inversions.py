def merge(arr, low, mid, high):
    left = arr[low : mid+1]
    right = arr[mid+1 : high+1]

    i = 0
    j = 0
    k = low
    cnt = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1

        else:
            arr[k] = right[j]
            cnt += len(left) - i
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

    return cnt

def merge_sort(arr, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2

        cnt += merge_sort(arr, low, mid)
        cnt += merge_sort(arr, mid + 1, high)

        cnt += merge(arr, low, mid, high)

    return cnt

arr = [2, 4, 1, 3, 5]
print(merge_sort(arr, 0, len(arr) - 1))
print(arr)

