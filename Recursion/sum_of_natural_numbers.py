def sum_natural_num(n):
    if n == 0 or n == 1:
        return n
    return n + sum_natural_num(n-1)

n = 10
print(sum_natural_num(n))