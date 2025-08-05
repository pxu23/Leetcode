def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    max_candies = 0
    for num_candy in candies:
        max_candies = max(max_candies, num_candy)

    result = []
    for num_candy in candies:
        if num_candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

if __name__ == '__main__':
    # Example 1
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))

    # Example 2
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(kidsWithCandies(candies, extraCandies))

    # Example 3
    candies = [12, 1, 12]
    extraCandies = 10
    print(kidsWithCandies(candies, extraCandies))