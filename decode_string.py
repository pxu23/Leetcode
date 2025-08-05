def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
            continue

        cur_str = ""
        while stack[-1] != "[":
            cur_str = stack.pop() + cur_str

        # pop off [
        stack.pop()

        cur_digit = ""
        while stack and stack[-1].isdigit():
            cur_digit = stack.pop() + cur_digit

        stack.append(int(cur_digit) * cur_str)

    return "".join([elem for elem in stack])

if __name__ == "__main__":
    # Example 1
    s = "3[a]2[bc]"
    print(decodeString(s))

    # Example 2
    s = "3[a2[c]]"
    print(decodeString(s))

    # Example 3
    s = "2[abc]3[cd]ef"
    print(decodeString(s))