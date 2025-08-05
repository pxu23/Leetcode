from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res = defaultdict(list)
    for s in strs:
        counts = 26 * [0]
        for c in s:
            counts[ord(c) - ord('a')] += 1

        counts_tuple = tuple(counts)
        res[counts_tuple].append(s)

    return res.values()

if __name__ == '__main__':
    # Example 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

    # Example 2
    strs = [""]
    print(groupAnagrams(strs))

    # Example 3
    strs = ["a"]
    print(groupAnagrams(strs))