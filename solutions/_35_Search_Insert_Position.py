import pytest
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1


class TestCase:
    def test_target_in_list(self):
        self.nums = [1, 3, 5, 6]
        self.target = 5
        self.res = 2
        assert searchInsert(self.nums, self.target) == self.res

    def test_target_not_in_list_inside(self):
        self.nums = [1, 3, 5, 6]
        self.target = 2
        self.res = 1
        assert searchInsert(self.nums, self.target) == self.res

    def test_target_not_in_list_outside(self):
        self.nums = [1, 3, 5, 6]
        self.target = 7
        self.res = 4
        assert searchInsert(self.nums, self.target) == self.res


if __name__ == '__main__':
    pytest.main()
