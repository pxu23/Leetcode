def removeStars(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []

    for c in s:
        if c != "*":
            stack.append(c)
        else:
            stack.pop()

    return "".join(stack)

if __name__=="__main__":
    # Example 1
    s = "leet**cod*e"
    print(removeStars(s))

    # Example 2
    s = "erase*****"
    print(removeStars(s))