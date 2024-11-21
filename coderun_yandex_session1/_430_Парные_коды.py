
import time
from itertools import combinations


def timer(func):
    def wrapper(*args, **kwargs):
        _start = time.time()
        result = func(*args, **kwargs)
        _end = time.time()
        print(f"Время выполнения: {_end - _start:.2f}")
        return result

    return wrapper


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


@timer
def main():
    # nums = [103, 123, 20, 4567]
    nums = range(3_00)
    combs = combinations(nums, 2)
    result = [find_common_digit(comb) for comb in combs]
    return sum(result)


if __name__ == '__main__':
    print(main())
