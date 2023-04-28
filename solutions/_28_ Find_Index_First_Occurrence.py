def strStr(haystack: str, needle: str) -> int:
    for idx, char in enumerate(haystack):
        if char == needle[0] and haystack[idx:idx+len(needle)] == needle:
            return idx
    return -1


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
