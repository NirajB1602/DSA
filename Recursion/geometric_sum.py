# for series 1 + 1/2 + 1/4 + 1/8 + ..... + 1/2**k
def geo_sum(k):
    if k == 0:
        return 1
    return 1/(2** (k)) + geo_sum(k-1)

print(geo_sum(3))


# for any series
def geo_sum(n, k):
    if k == 0:
        return 1
    return 1/(n**k) + geo_sum(n, k-1)

print(geo_sum(3, 5))