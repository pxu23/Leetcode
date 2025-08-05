from collections import Counter

def canConstruct(ransomNote, magazine):
    hashmap = Counter()

    for c in magazine:
        hashmap[c] += 1

    for c1 in ransomNote:
        if c1 not in hashmap:
            return False
        hashmap[c1] -= 1
        if hashmap[c1] == 0:
            del hashmap[c1]
    return True

if __name__ == '__main__':
    # Example 1
    ransomNote = "a"
    magazine = "b"
    print(canConstruct(ransomNote, magazine))

    # Example 2
    ransomNote = "aa"
    magazine = "bb"
    print(canConstruct(ransomNote, magazine))

    # Example 3
    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))