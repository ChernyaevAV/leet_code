from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    previous = dict()

    for idx, value in enumerate(nums):
        search_value = target - nums[idx]
        if search_value in previous:
            return [previous[search_value], idx]
        previous[value] = idx


if __name__ == '__main__':

    assert [1, 2] == twoSum([3, 2, 4], 6)
    assert [0, 1] == twoSum([0, 0], 0)
    assert [1, 2] == twoSum([0, -1, 5, 12, 3], 4)
