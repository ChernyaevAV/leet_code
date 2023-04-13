from typing import List


def removeElement(nums: List[int], val: int) -> int:
    count = 0
    left = 0
    for idx in range(len(nums)):
        if nums[idx] != val:
            nums[left], nums[idx] = nums[idx], nums[left]
            left += 1
            count += 1
        else:
            nums[idx] = ''

    return count


if __name__ == '__main__':
    nums = [1,1,2,2,2,3,4,4]
    res= removeElement(nums, 2)
    print(res)
    print(nums)
    assert res == 5
    assert nums[:res] == [1,1,3,4,4]