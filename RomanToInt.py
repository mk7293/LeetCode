def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s) - 1):
        if dict[s[i]] < dict[s[i + 1]]:
            total -= dict[s[i]]
        else:
            total += dict[s[i]]

    total += dict[s[len(s) - 1]]
    return total


if __name__ == '__main__':
    print(romanToInt('III'))
