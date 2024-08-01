
from datetime import datetime
from itertools import combinations


def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == target:
            return True
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


def find_common_digit(comb):
    if comb[0] <= comb[1]:
        set_min = set(str(comb[0]))
        set_max = set(str(comb[1]))
    else:
        set_min = set(str(comb[1]))
        set_max = set(str(comb[0]))

    for element in set_min:
        if element in set_max:
            return True
    return False


def main():
    # nums = [103, 123, 20, 4567]
    nums = range(3_000)
    combs = combinations(nums, 2)
    result = [find_common_digit(comb) for comb in combs]
    return sum(result)


if __name__ == '__main__':
    start = datetime.now()
    print(main())
    print((datetime.now() - start).total_seconds())
