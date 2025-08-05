def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    visited = set(nums)
    max_length = 0
    for elem in visited:

        if elem - 1 not in visited:
            cur_length = 1
            y = elem + 1
            while y in visited:
                cur_length += 1
                y += 1
            max_length = max(max_length, cur_length)

    return max_length

if __name__=='__main__':
    # Example 1
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))

    # Example 2
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(nums))

    # Example 3
    nums = [1, 0, 1, 2]
    print(longestConsecutive(nums))