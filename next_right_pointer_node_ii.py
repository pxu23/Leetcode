# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            for i in range(n):
                cur_node = queue.popleft()
                if i == n - 1:
                    next_node = None
                else:
                    next_node = queue[0]
                cur_node.next = next_node

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

        return root