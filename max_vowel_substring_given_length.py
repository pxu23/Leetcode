def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    max_vowel = 0

    vowels = set(["a", "e", "i", "o", "u"])
    r = 0
    vowel_in_window = 0

    for j in range(k):
        if s[r] in vowels:
            vowel_in_window += 1
        r += 1
    max_vowel = max(max_vowel, vowel_in_window)

    while r < len(s):
        if s[r - k] in vowels:
            vowel_in_window -= 1
        if s[r] in vowels:
            vowel_in_window += 1
        r += 1

        max_vowel = max(max_vowel, vowel_in_window)

    return max_vowel

if __name__=="__main__":
    # Example 1
    s = "abciiidef"
    k = 3
    print(maxVowels(s, k))

    # Example 2
    s = "aeiou"
    k = 2
    print(maxVowels(s, k))

    # Example 3
    s = "leetcode"
    k = 3
    print(maxVowels(s, k))