def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    low = 1

    # maximum value of piles
    max_val = 0
    for val in piles:
        max_val = max(val, max_val)

    high = max_val

    def canFinish(piles, k, h):
        num_hours = 0
        for i in range(len(piles)):
            added_val = piles[i] // k if piles[i] % k == 0 else piles[i] // k + 1
            num_hours = num_hours + added_val
        return num_hours <= h

    while low <= high:
        mid = (low + high) // 2
        if not canFinish(piles, mid, h):
            low = mid + 1
        if canFinish(piles, mid, h):
            if mid == 1:
                return 1
            if canFinish(piles, mid - 1, h):
                high = mid - 1
            else:
                return mid

    return -1

if __name__=="__main__":
    # Example 1
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))

    # Example 2
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(minEatingSpeed(piles, h))

    # Example 3
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(minEatingSpeed(piles, h))