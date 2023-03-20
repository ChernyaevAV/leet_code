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


class TestMyAtoi:
    def test_words_after(self):
        res = myAtoi('4193 with words')
        assert res == 4193

    def test_space_before_nums(self):
        res = myAtoi('   -42')
        assert res == -42

    def test_plus_before_nums(self):
        res = myAtoi('+53')
        assert res == 53

    def test_nums_after_words(self):
        res = myAtoi('words and 987')
        assert res == 0

    def test_dot_in_string(self):
        res = myAtoi('-3.14159')
        assert res == -3

    def test_more_symbols_before_nums(self):
        res = myAtoi('-+15')
        assert res == 0