from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            sub_arr_sum = 0
            for j in range(i, len(arr)):
                sub_arr_sum += arr[j]
                if sub_arr_sum % 2 != 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    arr = [1, 3, 5]
    ans = 4
    assert Solution().numOfSubarrays(arr) == ans

    arr = [2, 4, 6]
    ans = 0
    assert Solution().numOfSubarrays(arr) == ans

    arr = [1, 2, 3, 4, 5, 6, 7]
    ans = 16
    assert Solution().numOfSubarrays(arr) == ans