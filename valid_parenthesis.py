def validParenthesis(s):
    """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:
        1) Open brackets must be closed by the same type of brackets.
        2) Open brackets must be closed in the correct order.
        3) Evey close bracket has a corresponding open bracket of the same type.

        :param s: input string
        :return: True if s is valid string and False otherwise
    """
    opening_bracket = set(["(", "{", "["])
    closing_bracket = set([")", "}", "]"])

    open_close_match = {")":"(", "}":"{", "]":"["}

    stk = []
    for c in s:
        if c in opening_bracket:
            # push the opening bracket to the stack
            stk.append(c)
        elif c in closing_bracket:
            # encountered a closing bracket
            # if stack is empty then return False
            if len(stk) == 0:
                return False
            top = stk[-1]
            # no match found then False
            if open_close_match[c] != top:
                return False
            # pop the match off the stack
            stk.pop()
    # if stack not empty at end, then False
    if len(stk) > 0:
        return False
    return True

if __name__ == '__main__':
    # Example 1
    s = "()"
    print(validParenthesis(s))

    # Example 2
    s = "()[]{}"
    print(validParenthesis(s))

    # Example 3
    s = "(]"
    print(validParenthesis(s))

    # Example 4
    s = "([])"
    print(validParenthesis(s))