def steps(number):
    count = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            count += 1
        else:
            number = number * 3 + 1
            count += 1
    return count


try:
    assert steps(12) == 9
    steps(0)
except ValueError as e:
    assert str(e) == "Only positive integers are allowed"