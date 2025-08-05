import math


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    freq = {}
    for elem in nums:
        freq[elem] = freq.get(elem, 0) + 1

    n = len(nums)
    res = []
    visited = set()
    for elem in nums:
        if freq[elem] > math.floor(n / 3) and elem not in visited:
            res.append(elem)
            visited.add(elem)
    return res

if __name__ == '__main__':
    # Example 1
    nums = [3, 2, 3]
    print(majorityElement(nums))

    # Example 2
    nums = [1]
    print(majorityElement(nums))

    # Example 3
    nums = [1, 2]
    print(majorityElement(nums))