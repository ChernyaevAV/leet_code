import unittest
from roman_to_arab import romanToInt, romanToInt_2


class TestRomanToInt(unittest.TestCase):
    def test_roman_to_int(self):
        roman = 'MCMXCIV'
        self.assertEqual(1994, romanToInt(roman), 'Неверные вычисления')
        self.assertEqual(1994, romanToInt_2(roman), 'Неверные вычисления')

    def test_type_value(self):
        roman = 'xxiвек'
        self.assertNotIn(roman, romanToInt(roman),
                         'Римское число должно только из заглавных латинских букв')
