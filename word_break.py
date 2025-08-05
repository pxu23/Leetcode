def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    len_s = len(s)
    res = [False] * len_s

    for i in range(len(s)):
        substr = s[:i + 1]
        flag = False
        for word in wordDict:
            l_word = len(word)
            if substr.endswith(word):
                if len(s[:i - l_word + 1]) == 0 or res[i - l_word]:
                    flag = True
                    break
        res[i] = flag
    return res[len_s - 1]

if __name__ == '__main__':
    # Example 1
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s, wordDict))

    # Example 2
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict))

    # Example 3
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict))