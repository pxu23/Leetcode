from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestZigZag(root) -> int:
    stack = [root]

    # zigzag paths through node
    zigzag_path_through_node = defaultdict(list)
    zigzag_path_through_node[root].append((0, "L"))
    zigzag_path_through_node[root].append((0, "R"))

    longest_path = float('-inf')

    while stack:
        cur_node = stack.pop()
        for path_length, direction in zigzag_path_through_node[cur_node]:
            longest_path = max(longest_path, path_length)

        if cur_node.right:
            for path_length, direction in zigzag_path_through_node[cur_node]:
                if direction == "R":
                    zigzag_path_through_node[cur_node.right].append((path_length + 1, "L"))
                    zigzag_path_through_node[cur_node.right].append((0, "R"))
            stack.append(cur_node.right)

        if cur_node.left:
            for path_length, direction in zigzag_path_through_node[cur_node]:
                if direction == "L":
                    zigzag_path_through_node[cur_node.left].append((path_length + 1, "R"))
                    zigzag_path_through_node[cur_node.left].append((0, "L"))
            stack.append(cur_node.left)

    return longest_path