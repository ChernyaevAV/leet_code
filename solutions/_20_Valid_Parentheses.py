import pytest

def isValid(s: str) -> bool:
    valid_parents_open = '([{'
    valid_parents_closed = ')]}'
    valid_parents = ['()', '[]', '{}']
    stack = []
    for elem in s:
        if elem in valid_parents_open:
            stack.append(elem)
        if elem in valid_parents_closed:
            if stack and stack[-1] + elem in valid_parents:
                stack.pop()
            else:
                return False

    return len(stack) == 0


class TestCase:
    @staticmethod
    def test_one_parent():
        res = isValid('(')
        assert res == False

        res = isValid('[')
        assert res == False

        res = isValid('}')
        assert res == False

    @staticmethod
    def test_valid():
        res = isValid('()')
        assert res == True

        res = isValid('[]')
        assert res == True

        res = isValid('{}')
        assert res == True

    @staticmethod
    def test_three_parent():
        res = isValid('({}')
        assert res == False

        res = isValid('()}')
        assert res == False

        res = isValid('[](')
        assert res == False


if __name__ == '__main__':
    pass
