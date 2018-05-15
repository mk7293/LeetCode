def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""

    arr = list(strs[0])
    min_count = len(strs[0])

    for i in range(1, len(strs)):
        count = 0
        arr2 = list(strs[i])
        for j in range(len(arr2)):
            if j <= len(arr) - 1 and arr[j] == arr2[j]:
                count += 1
            else:
                if count == 0:
                    return ""
                break

        if min_count > count:
            min_count = count

    return "".join(arr[:min_count])


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))
