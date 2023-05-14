import pytest

def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split()[-1])


def test_one_space():
    s = "Hello World"
    assert lengthOfLastWord(s) == 5

def test_space_in_tail():
    s = "   fly me   to   the moon  "
    assert lengthOfLastWord(s) == 4

def test_more_words():
    s = "luffy is still joyboy"
    assert lengthOfLastWord(s) == 6

