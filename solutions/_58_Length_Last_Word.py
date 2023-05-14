def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split()[-1])


if __name__ == '__main__':
    s = "Hello World"
    res = lengthOfLastWord(s)
    answer = 5
    assert res == answer, f'ожидали {answer}, получили {res}'

    s = "   fly me   to   the moon  "
    res = lengthOfLastWord(s)
    answer = 4
    assert res == answer, f'ожидали {answer}, получили {res}'

    s = "luffy is still joyboy"
    res = lengthOfLastWord(s)
    answer = 6
    assert res == answer, f'ожидали {answer}, получили {res}'