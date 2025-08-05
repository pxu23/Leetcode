import heapq

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    freq = {}

    for val in nums:
        freq[val] = freq.get(val, 0) + 1

    heap = []
    for key, val in freq.items():
        heapq.heappush(heap, (-1 * val, key))

    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res

if __name__=="__main__":
    # Example 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))

    # Example 2
    nums = [1]
    k = 1
    print(topKFrequent(nums, k))