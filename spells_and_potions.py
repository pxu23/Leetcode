def successfulPairs(spells, potions, success):
    """
    :type spells: List[int]
    :type potions: List[int]
    :type success: int
    :rtype: List[int]
    """
    potions.sort()

    pairs = [0] * len(spells)
    # loop through the spells
    for i in range(len(spells)):
        cur_spell = spells[i]
        low, high = 0, len(potions) - 1

        while low <= high:
            mid = (low + high) // 2
            if cur_spell * potions[mid] < success:
                low = mid + 1
            elif cur_spell * potions[mid] >= success:
                if mid == 0:
                    pairs[i] = len(potions)
                    break
                else:
                    if cur_spell * potions[mid - 1] < success:
                        pairs[i] = len(potions) - mid
                        break
                    else:
                        high = mid - 1
    return pairs

if __name__=="__main__":
    # Example 1
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(successfulPairs(spells, potions, success))

    # Example 2
    spells = [3, 1, 2]
    potions = [8, 5, 8]
    success = 16
    print(successfulPairs(spells, potions, success))