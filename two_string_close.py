import doctest


def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    if len(word1) != len(word2):
        return False

    freq_w1 = {}
    for c in word1:
        val = ord(c) - ord('a')
        freq_w1[val] = freq_w1.get(val, 0) + 1

    freq_w2 = {}
    for c in word2:
        val = ord(c) - ord('a')
        freq_w2[val] = freq_w2.get(val, 0) + 1

    return (sorted(freq_w1.keys()) == sorted(freq_w2.keys())
            and sorted(freq_w1.values()) == sorted(freq_w2.values()))

if __name__ == '__main__':
    # Example 1
    word1 = "abc"
    word2 = "bca"
    print(closeStrings(word1, word2))

    # Example 2
    word1 = "a"
    word2 = "aa"
    print(closeStrings(word1, word2))

    # Example 3
    word1 = "cabbba"
    word2 = "abbccc"
    print(closeStrings(word1, word2))