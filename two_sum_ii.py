def twoSum(nums, target):
    """
        Works just like two sum except that the array is sorted
        :param nums: the input array that is sorted
        :param target: the target sum
        :return: the indices of the two elements that add up to target
    """
    l, r = 0, len(nums) - 1

    while l < r:
        two_sum = nums[l] + nums[r]
        if two_sum > target:
            r -= 1
        elif two_sum < target:
            l += 1
        else:
            return [l + 1, r + 1]

    return [-1, -1]

if __name__ == '__main__':
    # Example 1
    numbers = [2, 7, 11, 15]
    target = 9
    assert twoSum(numbers, target) == [1, 2]

    # Example 2
    numbers = [2, 3, 4]
    target = 6
    assert twoSum(numbers, target) == [1, 3]

    # Example 3
    numbers = [-1, 0]
    target = -1
    assert twoSum(numbers, target) == [1, 2]

    print("All tests passed")