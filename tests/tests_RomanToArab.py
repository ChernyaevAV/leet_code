import unittest
import pytest

import roman_to_arab
from roman_to_arab import romanToInt, roman_to_int_2


class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int(self):
        roman = 'MCMXCIV'
        self.assertEqual(1994, romanToInt(roman), 'Неверные вычисления')
        self.assertEqual(1994, roman_to_int_2(roman), 'Неверные вычисления')

    def test_type_value(self):
        roman = 'xxiвек'
        self.assertNotIn(
            roman,
            roman_to_arab.symbolToIntDict,
            'Римское число должно только из латинских букв IVXLCDM')


class TestCase:
    @staticmethod
    def test_valid_result_to_arab():
        res = romanToInt('MCMXCIV')
        assert res == 1994
        res2 = roman_to_int_2('XXI')
        assert res2 == 21

    @staticmethod
    def test_valid_roman_data():
        with pytest.raises(
                ValueError,
                match=r"Римское число должно только из заглавных латинских букв"
        ):
            roman_to_int_2('xxiвек')

