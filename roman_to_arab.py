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


def romanToInt_2(s: str) -> int:
    prevValue = symbolToIntDict["M"]
    totalValue = 0
    for c in s:
        currentValue = symbolToIntDict[c]
        if prevValue < currentValue:
            totalValue -= prevValue * 2
        totalValue += currentValue
        prevValue = currentValue
    return totalValue


if __name__ == '__main__':
    num = 'MCMXCIV'
    print(romanToInt_2(num))
