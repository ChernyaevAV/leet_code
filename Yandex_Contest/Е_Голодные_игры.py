# Написать класс, принимающий на вход текст
# задание 1: один метод класса должен выводить в консоль самое длинное слово
# задание 2: второй метод - самое часто встречающееся слово
# задание 3: третий метод выводит количество спецсимволов в тесте
# (точки, запятые и т.д.)
# задание 4: четвертый метод выводит все палиндромы
from string import punctuation

class Text:
    @staticmethod
    def valid_value(value):
        if not isinstance(value, str):
            raise ValueError('Ожидалась строка')
        return True

    def __init__(self, text):
        if self.valid_value(text):
            self.text = text

    def longest_word(self):
        words = self.text.split(' ')
        words = list(map(lambda w: w.strip('.,!@#$%^&*:;'), words))
        return max(words)

    def get_spec_symbols(self):
        spec = list(map(lambda w: w if w in punctuation else '', self.text))
        return ''.join(spec)

    def palindroms(self):
        words = self.text.split(' ')
        words = list(map(lambda w: w.strip('.,!@#$%^&*:;'), words))
        palindroms = [p for p in words if p == p[::-1] and len(p)>1]
        return palindroms


if __name__ == '__main__':
    s1 = 111
    try:
        Text(s1)
    except ValueError as e:
        assert e.__str__() == 'Ожидалась строка'

    s2 = 'asd. fdrgtre, dfgr!'
    assert Text(s2).longest_word() == 'fdrgtre'

    s3 = '!@#$%'
    assert Text(s3).longest_word() == ''

    s4 = 'aba dfg fgf ghhg a'
    assert Text(s4).palindroms() == ['aba', 'fgf', 'ghhg']

    s3 = '!@#$%'
    assert Text(s3).get_spec_symbols() == '!@#$%'