from typing import List


def compress(chars: List[str]) -> int:
    char_dict = {}
    for symbol in chars:
        char_dict[symbol] = char_dict.get(symbol, 0) + 1

    s = []
    for key, value in char_dict.items():
        s.append(key)
        if value >= 10:
            for i in str(value):
                s.append(str(i))
        else:
            s.append(value)
    chars = s
    return len(s)


if __name__ == '__main__':
    chars = ["a","a","b","b","c","c","c"]

    print(compress(chars))