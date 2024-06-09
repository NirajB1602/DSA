def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

arr = [9, 8, 7, 6, 5, 4, 3, 2, 2, 1]
insertion_sort(arr)
print(arr)