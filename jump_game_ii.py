def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = [0] * len(nums)

    for i in range(len(nums) - 2, -1, -1):
        max_jump = nums[i]
        min_jumps_from_cur_pos = float('inf')
        for j in range(1, max_jump + 1):
            if i + j >= len(nums):
                continue
            min_jumps_from_cur_pos = min(min_jumps_from_cur_pos,
                                         1 + res[i + j])

        res[i] = min_jumps_from_cur_pos
    return res[0]

if __name__ == '__main__':
    # Example 1
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))

    # Example 2
    nums = [2, 3, 0, 1, 4]
    print(jump(nums))