def QuadraticProbing(hash, hashSize, arr):
    counter = 0
        
    for i in arr:
        hash_key = i % hashSize
        temp_key = hash_key
        ptr = 1
                
        while hash[temp_key] != -1:
            if counter == hashSize or hash[temp_key] == i:
               break
                    
            temp_key = (hash_key + ptr ** 2) % hashSize
            ptr += 1
                    
            if temp_key == hash_key:
                break
                    
        if hash[temp_key] == -1:
            hash[temp_key] = i
                    
            
    return hash

hashSize = 11
arr = [21,10,32,43]
hash = [-1] * hashSize

print(QuadraticProbing(hash, hashSize, arr))