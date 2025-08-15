def reverseOnlyLetters(s):
    """
    :type s: str
    :rtype: str
    """

    def is_english_letter(c):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return True
        elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return True
        return False

    res = [c for c in s]

    left = 0
    right = len(s) - 1

    while left <= right:
        if not is_english_letter(s[left]):
            left += 1
            continue

        if not is_english_letter(s[right]):
            right -= 1
            continue

        temp = res[left]
        res[left] = res[right]
        res[right] = temp

        left += 1
        right -= 1

    return "".join([c for c in res])

if __name__=="__main__":
    # Example 1
    s = "ab-cd"
    print(reverseOnlyLetters(s))

    # Example 2
    s = "a-bc-dEf-ghIj"
    print(reverseOnlyLetters(s))

    # Example 3
    s = "Test1ng-Leet=code-Q!"
    print(reverseOnlyLetters(s))