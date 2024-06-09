def linearProbing(hashSize, arr):
    hash_table = [-1] * hashSize
        
    for i in arr:
        hash_key = i % hashSize
        temp_key = hash_key
            
        while hash_table[temp_key] != -1:
            if hash_table[temp_key] == i:
               break
                
            temp_key = (temp_key + 1) % hashSize
                
            if temp_key == hash_key:
                break
                
        if hash_table[temp_key] == -1:
            hash_table[temp_key] = i
                
        
    return hash_table

hashSize = 10
arr = [4,14,24,44]

print(linearProbing(hashSize, arr))