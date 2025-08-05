def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"

    cur_res = "1"  # n = 1
    for i in range(1, n):
        # continue to perform run length encoding
        rle = ""
        count = 0
        for i in range(len(cur_res)):
            if i > 0 and cur_res[i] != cur_res[i - 1]:
                rle = rle + str(count) + cur_res[i - 1]
                count = 1
            else:
                count += 1
        rle = rle + str(count) + cur_res[len(cur_res) - 1]
        cur_res = rle

    return cur_res

if __name__ == "__main__":
    # Example 1
    n = 4
    print(countAndSay(n))

    # Example 2
    n = 1
    print(countAndSay(n))