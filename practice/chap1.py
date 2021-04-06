def factors(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


# for values in factors(100):
#     print(values)


def factors_improve(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k = k + 1
    if k * k == n:
        yield k


for values in factors_improve(100):
    print(values)
