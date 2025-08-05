from collections import Counter

def getHint(secret: str, guess: str) -> str:
    num_bulls = 0
    num_crows = 0

    visited_freq_secret = Counter(secret)

    hashmap_secret = {}
    for i, digit in enumerate(secret):
        hashmap_secret[(digit, i)] = 1

    hashmap_guess = {}
    for i, digit in enumerate(guess):
        hashmap_guess[(digit, i)] = 1

    is_bull = [False] * len(guess)
    # remove all the bulls
    for i, digit in enumerate(guess):
        if (digit, i) in hashmap_secret:
            num_bulls += 1
            is_bull[i] = True
            visited_freq_secret[digit] -= 1
            if visited_freq_secret[digit] == 0:
                del visited_freq_secret[digit]

    # remove all the crows
    for i, digit in enumerate(guess):
        if is_bull[i]:
            continue

        if digit in visited_freq_secret:
            num_crows += 1
            visited_freq_secret[digit] -= 1
            if visited_freq_secret[digit] == 0:
                del visited_freq_secret[digit]

    output_str = str(num_bulls) + "A" + str(num_crows) + "B"
    return output_str

if __name__=="__main__":
    # Example 1
    secret = "1807"
    guess = "7810"
    print(getHint(secret, guess))

    # Example 2
    secret = "1123"
    guess = "0111"
    print(getHint(secret, guess))