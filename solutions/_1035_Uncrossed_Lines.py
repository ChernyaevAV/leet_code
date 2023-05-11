from typing import List


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    n1 = len(nums1)
    n2 = len(nums2)

    dp = [0] * (n2 + 1)
    dpPrev = [0] * (n2 + 1)

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[j] = 1 + dpPrev[j - 1]
            else:
                dp[j] = max(dp[j - 1], dpPrev[j])
        dpPrev = dp[:]

    return dp[n2]


if __name__ == '__main__':
    nums1 = [1, 4, 2]
    nums2 = [1, 2, 4]
    answer = 2
    result = maxUncrossedLines(nums1, nums2)
    assert result == answer, f'Получено: {result}, Ожидалось: {answer}'

    nums1 = [2, 5, 1, 2, 5]
    nums2 = [10, 5, 2, 1, 5, 2]
    answer = 3
    result = maxUncrossedLines(nums1, nums2)
    assert result == answer, f'Получено: {result}, Ожидалось: {answer}'

    nums1 = [1, 3, 7, 1, 7, 5]
    nums2 = [1, 9, 2, 5, 1]
    answer = 2
    result = maxUncrossedLines(nums1, nums2)
    assert result == answer, f'Получено: {result}, Ожидалось: {answer}'

    nums1 = [1, 1, 2, 1, 2]
    nums2 = [1, 3, 2, 3, 1]
    answer = 3
    result = maxUncrossedLines(nums1, nums2)
    assert result == answer, f'Получено: {result}, Ожидалось: {answer}'
