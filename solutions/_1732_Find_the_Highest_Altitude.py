from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for elem in gain:
            res.append(res[-1] + elem)
        return max(res)


class TestCase:
    def test1(self):
        gain = [-5, 1, 5, 0, -7]
        ans = 1
        assert Solution().largestAltitude(gain) == ans


    def test2(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]
        ans = 0
        assert Solution().largestAltitude(gain) == ans


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    ans = 1
    print(Solution().largestAltitude(gain))
