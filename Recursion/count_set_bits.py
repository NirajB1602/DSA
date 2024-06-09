def count_set_bits(n):
    if n == 0:
        return 0
    
    if n & 1 == 1:
        return 1 + count_set_bits(n >> 1)
    
    else:
        return count_set_bits(n >> 1)
    
n = 21
print(count_set_bits(n))