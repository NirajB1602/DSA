# Partition using naive approach

def partition(arr, pivot_idx):
    n = len(arr)
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[n-1] = arr[n-1], arr[pivot_idx]
    temp = []

    for i in arr:
        if i <= pivot:
            temp.append(i)  

    for i in arr:
        if i > pivot:
            temp.append(i)

    for i in range(n):
        arr[i] = temp[i]

arr = [2, 3, 5, 8, 7, 9, 10, 6, 2, 1]
pivot_idx = 7
partition(arr, pivot_idx)

print(arr)