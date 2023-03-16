def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False


if __name__ == '__main__':
    x = 121
    print(isPalindrome(x))
