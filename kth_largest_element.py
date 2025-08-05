import heapq

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return heapq.nlargest(k, nums)[-1]

if __name__=="__main__":
    # Example 1
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))

    # Example 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(findKthLargest(nums, k))