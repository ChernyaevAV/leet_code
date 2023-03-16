def longest_palindrome(s):
    n = len(s)
    max_len = 0
    start = 0
    for i in range(n):
        # проверяем палиндромы с центром в i
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            if max_len < (right - left + 1):
                max_len = right - left + 1
                start = left
            left -= 1
            right += 1
        # проверяем палиндромы с центром между i и i+1
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if max_len < (right - left + 1):
                max_len = right - left + 1
                start = left
            left -= 1
            right += 1
    return s[start:start+max_len]


if __name__ == '__main__':
    s = "abba"
    print(longest_palindrome(s))  # "bab"
