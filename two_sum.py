def twoSum(nums, target):
    """
        Find the indices of two distinct elements in nums array that adds up to target
        :param nums: the input array
        :param target: the target sum
        :return: the indices of two distinct elements in input array that add to sum
    """
    hashmap = {}
    for i in range(len(nums)):
        cur_elem = nums[i]
        remaining = target - cur_elem

        if remaining in hashmap:
            return [hashmap[remaining], i]
        else:
            hashmap[cur_elem] = i
    return [-1,1]


if __name__ == '__main__':
    # Example 1
    nums = [2,7,11,15]
    target = 9
    assert twoSum(nums, target) == [0,1]

    # Example 2
    nums = [3, 2, 4]
    target = 6
    assert twoSum(nums, target) == [1,2]

    # Example 3
    nums = [3, 3]
    target = 6
    assert twoSum(nums, target) == [0,1]

    print("All tests passed")