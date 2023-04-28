# def strStr(haystack: str, needle: str) -> int:
#     n = len(needle)
#     for idx, char in enumerate(haystack):
#         if char == needle[0] and haystack[idx:idx + n] == needle:
#             return idx
#     return -1

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# def strStr(haystack: str, needle: str) -> int:
#     m = len(needle)
#     n = len(haystack)
#     RADIX = 26
#     MOD = 1_000_000_033
#     MAX_WEIGHT = 1
#
#     if n < m:
#       return -1
#
#     for _ in range(m):
#         MAX_WEIGHT = (MAX_WEIGHT * RADIX) % MOD
#
#     def hash_value(string):
#         ans = 0
#         factor = 1
#
#         for i in range(m - 1, -1, -1):
#           ans += ((ord(string[i]) - 97) * (factor)) % MOD
#           factor = (factor * RADIX) % MOD
#
#         return ans % MOD
#
#     hash_needle = hash_value(needle)
#
#     for window_start in range(n - m + 1):
#         if window_start == 0:
#           hash_hay = hash_value(haystack)
#         else:
#             hash_hay = ((hash_hay * RADIX) % MOD
#                       - ((ord(haystack[window_start - 1]) - 97)
#                          * MAX_WEIGHT) % MOD
#                       + (ord(haystack[window_start + m - 1]) - 97)
#                       + MOD) % MOD
#
#         if hash_needle == hash_hay:
#             for i in range(m):
#                 if needle[i] != haystack[i + window_start]:
#                   break
#             if i == m - 1:
#               return window_start
#     return -1

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    assert strStr(haystack, needle) == 0

    haystack = "leetcode"
    needle = "leeto"
    assert strStr(haystack, needle) == -1

    haystack = "worldhello"
    needle = "ll"
    assert strStr(haystack, needle) == 7

    haystack = "a"
    needle = "a"
    assert strStr(haystack, needle) == 0

    haystack = "abc"
    needle = "c"
    assert strStr(haystack, needle) == 2

    haystack = "mississipi"
    needle = "issipi"
    assert strStr(haystack, needle) == 4