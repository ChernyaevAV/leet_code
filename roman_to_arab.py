symbolToIntDict = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000}

ROMAN_TO_INT = {'I': 1,
                'IV': 4,
                'V': 5,
                'IX': 9,
                'X': 10,
                'XL': 40,
                'L': 50,
                'XC': 90,
                'C': 100,
                'CD': 400,
                'D': 500,
                'CM': 900,
                'M': 1000
                }


def romanToInt(s: str) -> int:
    res = 0
    idx = 1
    while idx <= len(s):
        if s[idx] not in symbolToIntDict:
            raise ValueError(
                'Римское число должно только из латинских букв IVXLCDM'
            )
        if idx == len(s):
            res += ROMAN_TO_INT[s[idx - 1]]
            break
        temp = s[idx-1]+s[idx]
        if ROMAN_TO_INT.get(temp, 0):
            res += ROMAN_TO_INT.get(temp)
            idx += 2
            continue
        res += ROMAN_TO_INT[s[idx-1]]
        idx += 1
    return res


def roman_to_int_2(s: str) -> int:
    prev_value = symbolToIntDict["M"]
    total_value = 0
    for c in s:
        if c not in symbolToIntDict:
            raise ValueError(
                'Римское число должно только из заглавных латинских букв'
            )
        current_value = symbolToIntDict[c]
        if prev_value < current_value:
            total_value -= prev_value * 2
        total_value += current_value
        prev_value = current_value
    return total_value


if __name__ == '__main__':
    num = 'MCMXCIV'
    print(roman_to_int_2(num))
