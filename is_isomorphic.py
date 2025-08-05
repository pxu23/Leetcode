def isIsomorphic(s, t):
    hashmap = {}

    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = t[i]
        else:
            expected_val = hashmap[s[i]]
            if expected_val != t[i]:
                return False

    hashmap = {}

    for i in range(len(t)):
        if t[i] not in hashmap:
            hashmap[t[i]] = s[i]
        else:
            expected_val = hashmap[t[i]]
            if expected_val != s[i]:
                return False

    return True

if __name__ == "__main__":
    # Example 1
    s = "egg"
    t = "add"
    print(isIsomorphic(s, t))

    # Example 2
    s = "foo"
    t = "bar"
    print(isIsomorphic(s, t))

    # Example 3
    s = "paper"
    t = "title"
    print(isIsomorphic(s, t))