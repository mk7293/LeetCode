def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return len(nums)

    i = 0
    while i != len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i + 1]
        else:
            i = i + 1

    return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2]
    removeDuplicates(nums)