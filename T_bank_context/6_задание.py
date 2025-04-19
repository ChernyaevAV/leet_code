

def sep_list(lst):
    lst1 = [(1, idx+1) if val % 2 != 0 else (0, idx+1) for idx, val in enumerate(lst) if (idx + 1) % 2 != 0]
    lst2 = [(1, idx+1) if val % 2 == 0 else (0, idx+1) for idx, val in enumerate(lst) if (idx + 1) % 2 == 0]
    return lst1, lst2


def check_list(lst):
    return [val[1] for val in lst if val[0] == 0]


if __name__ == '__main__':
    # n = 2
    # lst = [2, 1, 6, 4]

    n = int(input())
    lst = list(map(int, input().split()))

    lst1, lst2 = sep_list(lst)
    res1 = check_list(lst1)
    res2 = check_list(lst2)
    if len(res1) == 1 and len(res2) == 1:
        print(*res1, *res2)
    else:
        print('-1 -1')
