def wordPattern(pattern, s):
    hashmap_pattern_str = {}
    hashmap_str_pattern = {}

    splitted_str = s.split(" ")

    if len(pattern) != len(splitted_str):
        return False

    for i in range(len(pattern)):
        if ((pattern[i] in hashmap_pattern_str and hashmap_pattern_str[pattern[i]] != splitted_str[i])
                or (splitted_str[i] in hashmap_str_pattern and hashmap_str_pattern[splitted_str[i]] != pattern[i])):
            return False
        hashmap_pattern_str[pattern[i]] = splitted_str[i]
        hashmap_str_pattern[splitted_str[i]] = pattern[i]
    return True

if __name__ == "__main__":
    # Example 1
    pattern = "abba"
    s = "dog cat cat dog"
    print(wordPattern(pattern, s))

    # Example 2
    pattern = "abba"
    s = "dog cat cat fish"
    print(wordPattern(pattern, s))

    # Example 3
    pattern = "aaaa"
    s = "dog cat cat dog"
    print(wordPattern(pattern, s))