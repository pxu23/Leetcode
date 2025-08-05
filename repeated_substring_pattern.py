def repeatedSubstringPattern(s: str) -> bool:
    for i in range(len(s) - 1):
        if len(s) % (i + 1) != 0:
            continue
        # print(i)
        num_times = len(s) // (i + 1)
        # print(num_times)
        # print(s[:i+1])
        # print(s[:i+1]* num_times)
        if s[:i + 1] * num_times == s:
            return True
    return False

if __name__ == '__main__':
    # Example 1
    s = "abab"
    print(repeatedSubstringPattern(s))

    # Example 2
    s = "aba"
    print(repeatedSubstringPattern(s))

    # Example 3
    s = "abcabcabcabc"
    print(repeatedSubstringPattern(s))