def sel(n):
    # n = int(input())

    res = n // 2 if n % 2 == 0 else (n + 1) // 2
    return res


assert sel(6) == 3
assert sel(5) == 3
assert sel(4) == 2
assert sel(7) == 4
assert sel(3) == 2
assert sel(11) == 6