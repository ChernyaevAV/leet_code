def encode(string):
    left = right = 0
    res = ""
    length = 0
    while left < len(string):
        while right < len(string) and string[left] == string[right]:
            right += 1
            length = len(string[left:right])
        if length == 1:
            res += string[left]
        else:
            res += str(length) + string[left]
        left = right
    return res


def decode(string):
    left = right = 0
    res = ""
    length = ""
    for idx, char in enumerate(string):
        if char.isdigit():
            length += char
        if char.isalpha() or char == " ":
            if length:
                res += int(length)*char
                length = ""
            else:
                res += char

    return res




assert encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB") == "12WB12W3B24WB"
assert decode("12WB12W3B24WB") == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
assert encode("AABBBCCCC") == "2A3B4C"
assert decode("2 hs2q q2w2 ") == "  hsqq qww  "