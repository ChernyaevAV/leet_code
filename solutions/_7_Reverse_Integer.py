def reverse2(x: int) -> int:
    temp_string = str(x)
    if temp_string[0] in '-':
        res = int(temp_string[0] + temp_string[:0:-1])
    else:
        res = int(temp_string[::-1])

    if (-2 ** 31) <= res <= (2 ** 31 - 1):
        return res
    else:
        return 0


def reverse(x: int) -> int:
    temp_string = str(abs(x))
    res = int(temp_string[::-1])
    if res > (2 ** 31 - 1):
        return 0
    else:
        return res if x > 0 else (res * -1)


if __name__ == '__main__':
    s = 1534236469
    print(f'число: {s}, перевертыш: {reverse(s)}') #0

    s = -321
    print(f'число: {s}, перевертыш: {reverse(s)}') #-123

    s = -120
    print(f'число: {s}, перевертыш: {reverse(s)}') #-21