def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]

    n = len(nums)
    for i in range(n):
        res = [elem + [j] for elem in res for j in nums if j not in elem]

    return res

if __name__ == '__main__':
    # Example 1
    nums = [1, 2, 3]
    print(permute(nums))

    # Example 2
    nums = [0, 1]
    print(permute(nums))

    # Example 3
    nums = [1]
    print(permute(nums))