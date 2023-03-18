from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    previous = dict()

    for idx, value in enumerate(nums):
        search_value = target - nums[idx]
        if search_value in previous:
            return [idx, previous[search_value]]
        previous[value] = idx


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6

    print(twoSum(nums, target))
