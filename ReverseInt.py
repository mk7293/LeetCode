import math


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    abs_x = abs(x)
    rev = 0
    while abs_x > 0:
        rev = (10 * rev) + (abs_x % 10)
        abs_x //= 10

    if rev >= math.pow(2, 31) - 1 or rev <= math.pow(-2, 31):
        return 0

    if x < 0:
        rev *= -1

    return rev;


if __name__ == '__main__':
    print(reverse(12345))
