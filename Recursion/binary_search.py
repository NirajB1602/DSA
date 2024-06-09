def binary_search(lst, low, high, x):
    if low > high:
        return -1
    mid = (low+high) // 2
    if lst[mid] == x:
        return mid
    elif lst[mid] > x:
        return binary_search(lst, low, mid - 1, x)
    else:
        return binary_search(lst, mid + 1, high, x)

print(binary_search([1, 2, 4, 5, 6, 8, 10], 0, 7, 6))