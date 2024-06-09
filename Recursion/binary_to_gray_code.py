def convert_binary_to_gray(num):
    if num == 0:
        return 0
    
    last_digit = num % 10
    second_last_digit = (num // 10) % 10

    if last_digit == second_last_digit:
        return 10 * convert_binary_to_gray(num // 10)
    
    else:
        return 1 + 10 * convert_binary_to_gray(num // 10)
    
num = 1001
print(convert_binary_to_gray(num))



