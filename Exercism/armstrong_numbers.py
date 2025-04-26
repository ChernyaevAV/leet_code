def is_armstrong_number(number):
    return sum([int(x) ** len(str(number)) for x in str(number)]) == number



assert is_armstrong_number(153) == True
assert is_armstrong_number(10) == False
assert is_armstrong_number(9) == True