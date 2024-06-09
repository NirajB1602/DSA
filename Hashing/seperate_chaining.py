def separateChaining(hashSize, arr):
    hash_table = [[] for i in range(hashSize)]
    for i in arr:
        key = i % hashSize
        hash_table[key].append(i)
            
    return hash_table

hashSize = 10
arr = [92,4,14,24,44,91]

print(separateChaining(hashSize, arr))
            