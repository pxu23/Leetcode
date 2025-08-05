def reverseDegree(s: str) -> int:
    reversed_degree = 0
    for i, c in enumerate(s):
        reversed_degree = reversed_degree + (26 - (ord(c) - ord('a'))) * (i + 1)

    return reversed_degree

if __name__ == '__main__':
    # Example 1
    s = "abc"
    print(reverseDegree(s))

    # Example 2
    s = "zaza"
    print(reverseDegree(s))