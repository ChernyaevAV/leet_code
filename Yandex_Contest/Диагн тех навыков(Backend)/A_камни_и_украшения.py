import sys

import pytest


def input_data():
    j = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()
    return j, s

def solution(s, j):
    result = 0
    for ch in s:
        if ch in j:
            result += 1
    return result

def main():
    j, s = input_data()
    print(solution(s, j))

class TestCase:
    def test_1(self):
        j = "ab"
        s = "abccdd"
        answer = 2
        assert solution(j, s)==answer

    def test_2(self):
        j = "ab"
        s = "aabbccdd"
        answer = 2
        assert solution(j, s)==answer

if __name__ == '__main__':
    # main()
    pytest.main()
