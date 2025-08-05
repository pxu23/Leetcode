def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    stack.append((temperatures[0], 0))

    for i in range(1, len(temperatures)):
        elem = temperatures[i]
        while len(stack) > 0 and elem > stack[-1][0]:
            top_elem, top_idx = stack[-1]
            res[top_idx] = i - top_idx
            stack.pop()
        stack.append((temperatures[i], i))

    return res

if __name__=="__main__":
    # Example 1
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))

    # Example 2
    temperatures = [30, 40, 50, 60]
    print(dailyTemperatures(temperatures))

    # Example 3
    temperatures = [30, 60, 90]
    print(dailyTemperatures(temperatures))