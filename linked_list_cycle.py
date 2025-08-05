def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    visited_node = set()
    cur_node = head

    while True:
        if not cur_node:
            break

        if cur_node in visited_node:
            return True

        visited_node.add(cur_node)
        cur_node = cur_node.next
    return False