from solutions.String_to_Integer_atoi import myAtoi


class TestMyAtoi:
    @staticmethod
    def test_words_after():
        res = myAtoi('4193 with words')
        assert res == 4193

    @staticmethod
    def test_space_before_nums():
        res = myAtoi('   -42')
        assert res == -42

    @staticmethod
    def test_plus_before_nums():
        res = myAtoi('+53')
        assert res == 53

    @staticmethod
    def test_nums_after_words():
        res = myAtoi('words and 987')
        assert res == 0

    @staticmethod
    def test_dot_in_string():
        res = myAtoi('-3.14159')
        assert res == -3

    @staticmethod
    def test_more_symbols_before_nums():
        res = myAtoi('-+15')
        assert res == 0
