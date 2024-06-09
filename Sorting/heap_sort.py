def heapify(arr, len_arr, ptr):
    maxi_idx = ptr
    left_node_idx = ptr * 2 + 1
    right_node_idx = ptr * 2 + 2

    if left_node_idx < len_arr and arr[left_node_idx] > arr[ptr]:
        maxi_idx = left_node_idx

    if right_node_idx < len_arr and arr[right_node_idx] > arr[maxi_idx]:
        maxi_idx = right_node_idx

    if maxi_idx != ptr:
        arr[maxi_idx], arr[ptr] = arr[ptr], arr[maxi_idx]
        heapify(arr, len_arr, maxi_idx) 

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)
