def get_nok(x, y):
    """ Возвращает Наименьшее Общее Кратное."""
    greater = max(x, y)
    while True:
        if (greater % x == 0) and (greater % y == 0):
            nok = greater
            break
        greater += 1
    return nok

def get_nod(x, y):
    """Возвращает Наибольший Общий Делитель"""
    # smaller = min(x, y)
    # for i in range(1, smaller + 1):
    #     if  (x % i == 0) and (y % i == 0):
    #         nod = i
    # return nod
    while x and y:
        if x>=y :
            x %= y
        else:
            y %= x
    return x | y



def main(nums):
    # nums = tuple(map(int, input().split()))
    nod = nums[0]
    nok = nums[1]
    mult = nok * nod
    res = []

    for a in range(1, mult + 1):
        if mult % a != 0:
            continue
        b = mult // a
        if get_nod(a, b) == nod:
            res.append((a, b))

    print(len(res))
    print(res)



if __name__ == '__main__':
    main([5, 10])