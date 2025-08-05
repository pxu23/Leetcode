def findDisappearedNumbers(nums):
    visited = set()
    for elem in nums:
        visited.add(elem)

    res = []
    n = len(nums)
    for i in range(1, n + 1):
        if i not in visited:
            res.append(i)
    return res

if __name__=='__main__':
    # Example 1
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))

    # Example 2
    nums = [1, 1]
    print(findDisappearedNumbers(nums))