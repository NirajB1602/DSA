def combination_for_last_digit(num):
    if num == 2:
        return "abc"
    if num == 3:
        return "def"
    if num == 4:
        return "ghi"
    if num == 5:
        return "jkl"
    if num == 6:
        return "mno"
    if num == 7:
        return "pqrs"
    if num == 8:
        return "tuv"
    if num == 9:
        return "wxyz"

def keypad_combination(num):
    if num <= 1:
        output = []
        output.append("")
        return output
    
    last_digit = num % 10
    remaining_digits = num // 10

    smallerOutput = keypad_combination(remaining_digits)
    output_for_last_digit = combination_for_last_digit(last_digit)
    output = []

    for substring in smallerOutput:
        for string in output_for_last_digit:
            res = substring + string
            output.append(res)

    return output

num = 2433
print(keypad_combination(num))
