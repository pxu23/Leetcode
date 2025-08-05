def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """

    for i in range(len(flowerbed)):
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
                return n <= 0

        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        else:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

    return n <= 0

if __name__ == '__main__':
    # Example 1
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))

    # Example 2
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(canPlaceFlowers(flowerbed, n))