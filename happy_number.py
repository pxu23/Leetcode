def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    num = n
    hashmap = {}
    while True:
        # sum of square of digits
        sum_sq_digits = 0
        curr_num = num
        while num > 0:
            digit = num % 10
            sum_sq_digits += digit ** 2
            #print(f"ssd is {sum_sq_digits}")
            num  = int(num / 10)
        if sum_sq_digits in hashmap:
            return False

        hashmap[curr_num] = sum_sq_digits
        #print(f"SSD is {sum_sq_digits}")
        if sum_sq_digits == 1:
            return True

        num = sum_sq_digits
    return False

if __name__ == '__main__':
    # Example 1
    n = 19
    print(isHappy(n))

    # Example 2
    n = 2
    print(isHappy(n))

    # Example 3
    n = 56
    print(isHappy(n))