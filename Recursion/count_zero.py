def count_zeros(num):
    if num == 0:
        return 0
    last_digit = num % 10 
    if last_digit == 0:
        return 1 + count_zeros(num // 10)
    else:
        return count_zeros(num // 10)
    
print(count_zeros(10000000060))