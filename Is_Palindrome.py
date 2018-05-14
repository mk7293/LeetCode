def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False

    rev = int(str(x)[::-1])
    if x == rev:
        return True

    return False


if __name__ == '__main__':
    print(isPalindrome(121))