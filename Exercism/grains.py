def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    return sum([square(i) for i in range(1, 65)])


assert square(1) == 1
assert square(2) == 2
assert square(3) == 4
assert square(4) == 8
assert square(16) == 32768
assert square(32) == 2147483648
assert square(64) == 9223372036854775808