from typing import List

import pytest


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1
        if i == 0 or i == N-1:
            return False
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1
        return i == N-1


class TestCase:
    def test1(self):
        arr = [2, 1]
        ans = False
        assert Solution().validMountainArray(arr) == ans

    def test2(self):
        arr = [3, 5, 5]
        ans = False
        assert Solution().validMountainArray(arr) == ans

    def test3(self):
        arr = [0, 3, 2, 1]
        ans = True
        assert Solution().validMountainArray(arr) == ans


if __name__ == '__main__':
    pytest.main()