import random


def main():
    # n = int(input())
    nums = '1 2 3 4 4'.split()
    nums_count = {}
    for elem in nums:
        nums_count[elem] = nums_count.get(elem, 0) + 1
    res = list(filter(lambda x: x == 1, nums_count.values()))
    print(len(res))


if __name__ == '__main__':
    main()
