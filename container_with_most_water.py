def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        #print(f"l is {l}")
        #print(f"r is {r}")
        area = (r - l) * min(height[l], height[r])
        max_area = max(area, max_area)

        if height[r] <= height[l]:
            r -= 1
        elif height[l] <= height[r]:
            l += 1
        #print(f"l is {l}, r is {r}")

    return max_area

if __name__ == '__main__':
    height = [3, 6, 1]
    print(maxArea(height))