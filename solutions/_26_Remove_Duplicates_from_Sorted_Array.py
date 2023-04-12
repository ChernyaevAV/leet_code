from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums_uniq = {}
    left = 0
    for idx in range(len(nums)):
        if nums[idx] not in nums_uniq:
            nums_uniq[nums[idx]] = idx
            nums[left], nums[idx] = nums[idx], nums[left]
            left += 1
        else:
            nums[idx] = ''
    return len(nums_uniq)


if __name__ == '__main__':
    nums = [1,1,2,2,2,3,4,4]
    res= removeDuplicates(nums)
    print(res)
    print(nums)
    assert res == 4
    assert nums[:res] == [1,2,3,4]