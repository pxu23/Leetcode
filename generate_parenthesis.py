from collections import deque


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    queue = deque()

    queue.append("(")

    def is_well_formed(s):
        stack = []
        well_formed = False
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != "(":
                    return False
                stack.pop()
        if stack:
            return False

        return True

    while queue:
        cur = queue.popleft()
        if len(cur) == 2 * n and is_well_formed(cur):
            res.append(cur)

        if len(cur) < 2 * n:
            for bracket in ["(", ")"]:
                new_cur = cur + bracket
                queue.append(new_cur)

    return res

if __name__ == '__main__':
    # Example 1
    n = 3
    print(generateParenthesis(n))

    # Example 2
    n = 1
    print(generateParenthesis(n))