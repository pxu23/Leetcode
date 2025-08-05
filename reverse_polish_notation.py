def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []

    operators = set(["+", "-", "*", "/"])
    for i in range(len(tokens)):
        if tokens[i] not in operators:
            stack.append(tokens[i])
            continue

        right = int(stack.pop())
        # print(right)
        left = int(stack.pop())
        # print(left)
        if tokens[i] == "+":
            stack.append(str(left + right))
        elif tokens[i] == "-":
            stack.append(str(left - right))
        elif tokens[i] == "*":
            stack.append(str(left * right))
        else:
            stack.append(str(left // right + 1) if left // right < 0 and left % right != 0 else str(left // right))

    return int(stack[-1])

if __name__=="__main__":
    # Example 1
    tokens = ["2", "1", "+", "3", "*"]
    print(evalRPN(tokens))

    # Example 2
    tokens = ["4", "13", "5", "/", "+"]
    print(evalRPN(tokens))

    # Example 3
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens))

