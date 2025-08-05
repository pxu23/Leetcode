def flipAndInvertImage(image):
    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(image)
    n = len(image[0])

    l = 0
    r = n - 1

    # flipping horizontally
    while l <= r:
        for i in range(m):
            temp = image[i][l]
            image[i][l] = image[i][r]
            image[i][r] = temp
        l += 1
        r -= 1

    for i in range(m):
        for j in range(n):
            if image[i][j] == 1:
                image[i][j] = 0
            else:
                image[i][j] = 1

    return image

if __name__=="__main__":
    # Example 1
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    print(flipAndInvertImage(image))

    # Example 2
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(flipAndInvertImage(image))