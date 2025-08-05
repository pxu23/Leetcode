from collections import Counter

def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    freq = Counter(nums)
    cnt = 0
    for elem in nums:
        # print(elem)
        # print(freq[elem])
        if freq[elem] == 0:
            continue

        if k - elem in freq:
            freq[elem] -= 1
            if freq[k - elem] == 0:
                freq[elem] += 1
                continue
            freq[k - elem] -= 1
            cnt += 1
    return cnt

if __name__=="__main__":
    # Example 1
    nums = [1, 2, 3, 4]
    k = 5
    print(maxOperations(nums, k))

    # Example 2
    nums = [3,1,3,4,3]
    k = 6
    print(maxOperations(nums, k))