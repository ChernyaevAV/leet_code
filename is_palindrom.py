def is_palindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False


if __name__ == '__main__':
    assert is_palindrome(121) is True
    assert is_palindrome(5225) is True
    assert is_palindrome(5222) is False
    assert is_palindrome(2002) is True
