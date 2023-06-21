from typing import List

import pytest


class Solution:
    def oddString(self, words: List[str]) -> str:
        res = {}
        for item in words:
            temp_diff = []
            for idx in range(1, len(item)):
                temp_diff.append(ord(item[idx]) - ord(item[idx-1]))
            diff = tuple(temp_diff)
            res[diff] = res.get(diff, []) + [item]

        for val in res.values():
            if len(val) == 1:
                return val[0]


class TestCase:
    def test1(self):
        words = ["adc", "wzy", "abc"]
        answer = "abc"
        assert Solution().oddString(words) == answer

    def test2(self):
        words = ["aaa", "bob", "ccc", "ddd"]
        answer = "bob"
        assert Solution().oddString(words) == answer

if __name__ == '__main__':
    # words = ["adc", "wzy", "abc"]
    # print(Solution().oddString(words))
    pytest.main()