def combinationSum2(candidates, target):
    res = []
    stack = []
    candidates.sort()
    visited = set()
    for i in range(len(candidates)):
        if candidates[i] in visited:
            continue
        if candidates[i] > target:
            continue
        elif candidates[i] == target:
            res.append([candidates[i]])
        else:
            stack.append([i])

        visited.add(candidates[i])

    while stack:
        cur_path_idx = stack.pop()

        last_idx = cur_path_idx[-1]

        cur_path = [candidates[i] for i in cur_path_idx]
        path_sum = sum(cur_path)

        visited = set()
        for j in range(last_idx + 1, len(candidates)):
            if candidates[j] in visited:
                continue
            if path_sum + candidates[j] > target:
                continue
            elif path_sum + candidates[j] == target:
                res.append(cur_path + [candidates[j]])
            else:
                stack.append(cur_path_idx + [j])
            visited.add(candidates[j])

    return res

if __name__ == "__main__":
    # Example 1
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combinationSum2(candidates, target))

    # Example 2
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(combinationSum2(candidates, target))