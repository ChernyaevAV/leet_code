from typing import List


def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    k = lf
    i = j = 0
    while lf + i < mid and mid + j < rg:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if lf + i < mid:
        while k < rg:
            arr[k] = left[i]
            i += 1
            k += 1

    else:
        while k < rg:
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def sortArray(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums)
    if right - left > 1:
        mid = (left + right) // 2
        sortArray(nums[left:mid])
        sortArray(nums[mid:right])
        return merge(nums, left, mid, right)


if __name__ == '__main__':
    array = [5, 1, 1, 2, 0, 0]
    print(sortArray(array))
