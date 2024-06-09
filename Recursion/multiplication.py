def mul(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    return num1 + mul(num1, num2 - 1)

print(mul(3, 5))
print(mul(3, 0))
print(mul(0, 5))
print(mul(100, 5))

