from collections import namedtuple
from functools import reduce
from itertools import permutations, combinations


class Number(namedtuple('Number', 'idx num')):
    pass

    def __repr__(self):
        return f'{self.num}'


def data_load():
    n = int(input().strip())
    num_list = input().split()
    return n, num_list


def main():
    nums = [0, 0, 0]
    list_comb = combinations(nums, 2)
    result = map(lambda x: len(set(str(x[0])).intersection(set(str(x[1])))) > 0, list_comb)
    return sum(result)


if __name__ == '__main__':
    # n, nums = data_load()
    res = main()

    print(res)                      # ToDO не проходят тесты по времени (3с)
