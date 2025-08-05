def rotateRight(head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    if not head:
        return head

    # length of list
    len_list = 1
    cur_node = head
    while cur_node.next:
        len_list += 1
        cur_node = cur_node.next
    k = k % len_list
    cur_node.next = head
    cur_node = cur_node.next

    for i in range(len_list - k - 1):
        cur_node = cur_node.next

    newHead = cur_node.next
    cur_node.next = None
    return newHead