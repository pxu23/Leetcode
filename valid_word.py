def isValid(word):
    """
    :type word: str
    :rtype: bool
    """
    num_vowels = 0
    num_consonants = 0

    if len(word) < 3:
        return False

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    for i in range(len(word)):
        if not word[i].isdigit():
            if not (ord(word[i]) >= ord("a") and ord(word[i]) <= ord("z")):
                if not (ord(word[i]) >= ord("A") and ord(word[i]) <= ord("Z")):
                    return False

        if word[i] in vowels:
            num_vowels += 1
        else:
            if not word[i].isdigit():
                num_consonants += 1

    return num_vowels >= 1 and num_consonants >= 1

if __name__ == '__main__':
    # Example 1
    word = "234Adas"
    print(isValid(word))

    # Example 2
    word = "b3"
    print(isValid(word))

    # Example 3
    word = "a3$e"
    print(isValid(word))