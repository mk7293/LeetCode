def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if s is None:
        return True

    stack = []
    list = ['[', '{', '(']
    dict = {'[': ']', '{': '}', '(': ')'}

    for i in range(len(s)):
        if s[i] in list:
            stack.insert(0, s[i])
        elif stack and dict[stack[0]] == s[i]:
            stack.pop(0)
        else:
            return False

    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isValid('([])'))
