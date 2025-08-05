def removeNthFromEnd(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    len_list = 0
    curr_node = head

    while curr_node:
        len_list += 1
        curr_node = curr_node.next

    if len_list == n:
        return head.next

    i = 0
    curr_node = head
    while curr_node:
        i += 1
        if i == len_list - n:
            curr_node.next = curr_node.next.next

        curr_node = curr_node.next

    return head