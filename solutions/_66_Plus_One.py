from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ''
        for n in digits:
            num_str += str(n)
        num_str = str(int(num_str) + 1)
        res = [int(i) for i in num_str]
        return res

    def plusOne2(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i in reversed(range(n)):
            val = digits[i] + carry + 1 if i == n - 1 else digits[i] + carry
            if val <= 9:
                digits[i] = val
                carry = 0
            else:
                carry = val // 10
                val -= 10
                digits[i] = val
        if carry:
            digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    digits = [1, 2, 9]
    ans = [1, 3, 0]
    assert ans == Solution().plusOne(digits)

    digits = [9]
    ans = [1, 0]
    assert ans == Solution().plusOne2(digits)