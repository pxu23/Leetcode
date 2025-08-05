def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    cur_char = chars[0]
    cnt = 1
    res_str = ""
    for i in range(1, len(chars)):
        if chars[i] != cur_char:
            res_str = res_str + cur_char if cnt == 1 else res_str + cur_char + str(cnt)
            cur_char = chars[i]
            cnt = 1
        else:
            cnt += 1

    res_str = res_str + cur_char if cnt == 1 else res_str + cur_char + str(cnt)
    for i in range(len(chars) - len(res_str)):
        chars.pop()

    for i in range(len(res_str) - 1, -1, -1):
        chars[i] = res_str[i]

    return len(res_str)

if __name__=="__main__":
    # Example 1
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(compress(chars))
    print(chars)

    # Example 2
    chars = ["a"]
    print(compress(chars))
    print(chars)

    # Example 3
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(compress(chars))
    print(chars)
