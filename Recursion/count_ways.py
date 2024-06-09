def count_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

print(count_ways(4))