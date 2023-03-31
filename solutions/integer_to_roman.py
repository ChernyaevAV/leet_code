def intToRoman(num: int) -> str:
    int_to_roman_dict = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L",
        40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",
    }
    roman_num = ''
    for arabic, roman in int_to_roman_dict.items():
        while num >= arabic:
            roman_num += roman
            num -= arabic
    return roman_num

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
