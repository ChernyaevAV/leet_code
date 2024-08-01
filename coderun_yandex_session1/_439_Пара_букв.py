from itertools import pairwise


def get_double(string: str) -> dict:
    """
    Находит такую пару латинских символов,
    которая чаще всего встречается в тексте в качестве подстроки.
    Например, «LL» является подстрокой в тексте «HELLO», а «HO» — нет.
    """
    words = [word for word in string.split() if len(word) > 1]
    res = dict()
    for word in words:
        for i, j in pairwise(word):
            res[i+j] = res.get(i+j, 0) + 1
    return res


def filter_and_select(dictionary):
    max_value = max(dictionary.values())
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    max_key = max(max_keys)
    return max_key


def main():
    s = input()
    print(filter_and_select(get_double(s)))


if __name__ == '__main__':
    main()