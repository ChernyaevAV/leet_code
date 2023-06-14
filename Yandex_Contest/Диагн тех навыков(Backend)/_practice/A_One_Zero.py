from typing import Tuple

import pytest


def input_data() -> Tuple[str, str]:
    str1 = input()
    str2 = input()
    return str1, str2


def convert_str_to_int(str1: str, str2: str) -> Tuple[int, int]:
    num1 = int(str1.replace('one', '1').replace('zero', '0'), 2)
    num2 = int(str2.replace('one', '1').replace('zero', '0'), 2)
    return num1, num2


def bin_compare(num1: int, num2: int) -> str:
    if num1 == num2:
        return '='
    elif num1 < num2:
        return '<'
    else:
        return '>'


def main():
    str1, str2 = input_data()
    num1, num2 = convert_str_to_int(str1, str2)
    print(bin_compare(num1, num2))


class TestCase:
    def test_1(self):
        self.str1 = 'oneone'
        self.str2 = 'onezerozero'
        self.num1, self.num2 = convert_str_to_int(self.str1, self.str2)
        self.res = bin_compare(self.num1, self.num2)
        self.answer = '<'
        assert self.res == self.answer

    def test_2(self):
        self.str1 = 'zero'
        self.str2 = 'zero'
        self.num1, self.num2 = convert_str_to_int(self.str1, self.str2)
        self.res = bin_compare(self.num1, self.num2)
        self.answer = '='
        assert self.res == self.answer

    def test_3(self):
        self.str1 = 'onezero'
        self.str2 = 'oneone'
        self.num1, self.num2 = convert_str_to_int(self.str1, self.str2)
        self.res = bin_compare(self.num1, self.num2)
        self.answer = '<'
        assert self.res == self.answer

    def test_4(self):
        self.str1 = 'oneonezerozero'
        self.str2 = 'onezeroonezero'
        self.num1, self.num2 = convert_str_to_int(self.str1, self.str2)
        self.res = bin_compare(self.num1, self.num2)
        self.answer = '>'
        assert self.res == self.answer


if __name__ == '__main__':
    # main()
    pytest.main()
