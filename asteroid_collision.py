def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    stack = []

    for ast in asteroids:
        if len(stack) == 0:
            stack.append(ast)
            continue

        if stack[-1] < 0:
            stack.append(ast)
            continue

        if stack[-1] > 0:
            if ast > 0:
                stack.append(ast)
                continue
            if ast < 0:
                to_append = False
                while len(stack) > 0 and stack[-1] > 0:
                    if stack[-1] > -1 * ast:
                        to_append = False
                        break
                    elif stack[-1] < -1 * ast:
                        stack.pop()
                        to_append = True
                    else:
                        to_append = False
                        stack.pop()
                        break
                if to_append:
                    stack.append(ast)
    return stack

if __name__=="__main__":
    # Example 1
    asteroids = [5, 10, -5]
    print(asteroidCollision(asteroids))

    # Example 2
    asteroids = [8, -8]
    print(asteroidCollision(asteroids))

    # Example 3
    asteroids = [10, 2, -5]
    print(asteroidCollision(asteroids))