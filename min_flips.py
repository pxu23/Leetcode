def minFlips(a: int, b: int, c: int) -> int:
    num_flips = 0
    while a > 0 or b > 0 or c > 0:
        #print(a)
        #print(b)
        a_bit = a % 2
        b_bit = b % 2
        c_bit = c % 2
        if a_bit | b_bit == c_bit:
            a = a >> 1
            b = b >> 1
            c = c >> 1
            continue

        num_bit_one_a_b = a_bit + b_bit

        if c_bit == 0:
            num_flips = num_flips + num_bit_one_a_b
        else:
            num_flips += 1

        a = a >> 1
        b = b >> 1
        c = c >> 1

    return num_flips

if __name__=="__main__":
    # Example 1
    a = 2
    b = 6
    c = 5
    print(minFlips(a, b, c))