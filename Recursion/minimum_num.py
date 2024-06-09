def minimum(arr, si, ans = 999999):
    ei = len(arr) - 1
    if si > ei:
        return ans
    if arr[si] < ans:
        ans = arr[si]
        return minimum(arr, si + 1, ans)
    else:
        return minimum(arr, si + 1, ans)

arr = [1, 2, 4, 6, 8, 10, 0]
print(minimum(arr, 0))
    