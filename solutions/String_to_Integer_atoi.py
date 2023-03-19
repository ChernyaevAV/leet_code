def myAtoi(s: str) -> int:
    s = s.strip()
    if s == '':
        return 0
    znak = -1 if s[0] == '-' else 1
    s = s[1:] if s[0] in '-+' else s
    res = 0
    for elem in s:
        if elem not in '0123456789':
            break
        res = res * 10 + int(elem)
        if res * znak >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res * znak <= -2 ** 31:
            return -2 ** 31
    return res * znak
