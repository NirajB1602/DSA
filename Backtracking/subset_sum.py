def find_subsets(arr, target, temp = [], si = 0):
    if target == 0:
        print(temp)
        return
    
    if si == len(arr):
        return
        
    find_subsets(arr, target, temp, si + 1)

    if arr[si] <= target:
        temp.append(arr[si])
        find_subsets(arr, target - arr[si], temp, si + 1)
        temp.pop()

arr = [1, 2, 1]
target = 3
find_subsets(arr, target)
    

