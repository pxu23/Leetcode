def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    vowel_pos = []

    for i in range(len(s)):
        if s[i] in vowels:
            vowel_pos.append((s[i], i))

    left = 0
    right = len(vowel_pos) - 1

    res_str = [c for c in s]
    while left <= right:
        first_vowel_pos = vowel_pos[left][1]
        first_vowel = vowel_pos[left][0]

        second_vowel_pos = vowel_pos[right][1]
        second_vowel = vowel_pos[right][0]

        res_str[first_vowel_pos] = second_vowel
        res_str[second_vowel_pos] = first_vowel

        left += 1
        right -= 1

    return "".join([c for c in res_str])

if __name__=="__main__":
    # Example 1
    s = "IceCreAm"
    print(reverseVowels(s))

    # Example 2
    s = "leetcode"
    print(reverseVowels(s))