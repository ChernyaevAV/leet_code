def get_nok(a, b):
    """ Возвращает Наименьшее Общее Кратное."""
    return a * b // get_nod(a, b)


def get_nod(a, b):
    """Возвращает Наибольший Общий Делитель"""
    while b:
        a, b = b, a % b
    return a


def main():
    nod, nok = tuple(map(int, input().split()))
    mult = nok * nod
    res = []

    for a in range(1, mult + 1):
        if mult % a != 0:
            continue
        b = mult // a
        if get_nod(a, b) == nod:
            res.append((a, b))
    print(len(res))


if __name__ == '__main__':
    main()

