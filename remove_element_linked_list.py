def removeElements(head, val):
    """
    :type head: Optional[ListNode]
    :type val: int
    :rtype: Optional[ListNode]
    """
    if not head:
        return

    curr_node = head

    while curr_node and curr_node.next:
        while curr_node.next and curr_node.next.val == val:
            curr_node.next = curr_node.next.next

        curr_node = curr_node.next

    if head.val == val:
        return head.next

    return head