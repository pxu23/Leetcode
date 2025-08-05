class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    visited = set()

    cur_node = head
    while cur_node:
        if cur_node in visited:
            return cur_node

        visited.add(cur_node)
        cur_node = cur_node.next
    return None