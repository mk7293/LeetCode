def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    tmp = {}

    for i in range(len(nums)):
        if target - nums[i] in tmp:
            return (tmp[target - nums[i]], i)
        else:
            tmp[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 9, 7, 11]
    print(twoSum(nums, 9))
