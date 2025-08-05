def simplifyPath(path: str) -> str:
    stack = []

    cur_directory = ""
    for i in range(len(path)):
        elem = path[i]

        if elem == "/":
            if cur_directory == "":
                if len(stack) > 0:
                    stack.pop()
            elif cur_directory == ".":
                if len(stack) > 0:
                    stack.pop()
            elif cur_directory == "..":
                for i in range(3):
                    if len(stack) == 0:
                        break
                    stack.pop()
            else:
                stack.append(cur_directory)

            stack.append("/")
            cur_directory = ""
        else:
            cur_directory = cur_directory + elem

    if cur_directory == ".":
        if len(stack) > 1:
            stack.pop()
    elif cur_directory == "..":
        for i in range(3):
            if len(stack) <= 1:
                break
            stack.pop()
    elif len(cur_directory) > 0:
        stack.append(cur_directory)

    if len(stack) > 1 and stack[-1] == "/":
        stack.pop()

    return "".join([elem for elem in stack])

if __name__=="__main__":
    # Example 1
    path = "/home//foo/"
    print(simplifyPath(path))

    # Example 2
    path = "/home/user/Documents/../Pictures"
    print(simplifyPath(path))

    # Example 3
    path = "/../"
    print(simplifyPath(path))