from collections import defaultdict

def suggestedProducts(products, searchWord: str):
    # get the words that start with a prefix
    prefix_string = defaultdict(list)
    for elem in products:
        for i in range(len(elem)):
            prefix = elem[:i + 1]
            prefix_string[prefix].append(elem)

    res = []
    for i in range(len(searchWord)):
        cur_prefix = searchWord[:i + 1]
        words_starting_with_cur_prefix = sorted(prefix_string[cur_prefix])

        res.append(words_starting_with_cur_prefix[:min(len(words_starting_with_cur_prefix), 3)])

    return res

if __name__=="__main__":
    # Example 1
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))

    # Example 2
    products = ["havana"]
    searchWord = "havana"
    print(suggestedProducts(products, searchWord))