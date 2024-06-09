def combination_sum(arr, target):
    arr = sorted(list(set(arr)))
    res = []

    def find_numbers(target, path):
        if target == 0:
            res.append(path)
            return 
        
        for i in range(len(arr)):
            if arr[i] > target:
                return
            
            find_numbers(target - arr[i], path + [arr[i]])
    
    find_numbers(target, [])
    return res

arr = [2, 4, 6, 8]
target = 8
print(combination_sum(arr, target))
