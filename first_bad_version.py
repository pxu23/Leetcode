import math

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    low = 0
    high = n

    while low <= high:
        mid = int(math.ceil(float(low + high) / 2))
        if isBadVersion(mid) == False:
            low = mid + 1
        else:
            if mid == 0:
                return 0
            if mid > 0:
                if isBadVersion(mid - 1) == False:
                    return mid
                else:
                    high = mid - 1
    return -1