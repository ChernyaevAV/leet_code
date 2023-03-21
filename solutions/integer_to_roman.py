def intToRoman(num: int) -> str:
    int_to_roman_dict = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    res = ''

    for elem in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while elem <= num:
            res += int_to_roman_dict[elem]
            num -= elem
    return res

class TestIntToRoman:
    def test_int_to_roman(self):
        year = 1994
        assert intToRoman(year) == "MCMXCIV"

    def test_lower_4(self):
        year = 3
        assert intToRoman(year) == "III"

    def test_100_and_10(self):
        year = 100
        assert intToRoman(year) == "C"
        year = 10
        assert intToRoman(year) == "X"


if __name__ == '__main__':
    year = 35
    print(intToRoman(year))
