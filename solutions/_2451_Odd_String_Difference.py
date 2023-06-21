from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        res = {}
        for item in words:
            diff = []
            for idx in range(1, len(item)):
                diff.append(ord(item[idx]) - ord(item[idx-1]))
            if diff not in res.values():
                res[diff] = res.get(diff, [])
        return res


if __name__ == '__main__':
    words = ["adc", "wzy", "abc"]
    print(Solution().oddString(words))
