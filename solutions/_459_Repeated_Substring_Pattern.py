def repeatedSubstringPattern(s: str) -> bool:
    if len(s) == 0:
        return True
    for idx in range(len(s)):
        if  len(s) % len(s[:idx+1]) != 0:
            continue
        if (s[:idx+1] * (len(s) // len(s[:idx+1])) == s
            and len(s) != len(s[:idx+1])):
            return True
    return False


# def repeatedSubstringPattern(s: str) -> bool:
#     if not s:
#         return False
#     ss = (s + s)[1:-1]
#     return ss.find(s) != -1


if __name__ == '__main__':
    s = "abab"
    assert repeatedSubstringPattern(s) == True

    s = "aba"
    assert repeatedSubstringPattern(s) == False

    s = "abcabcabcabc"
    assert repeatedSubstringPattern(s) == True

    s = "a"
    assert repeatedSubstringPattern(s) == False
