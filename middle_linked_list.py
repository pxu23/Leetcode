def middleNode(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    len_list = 0
    curr_node = head
    while curr_node:
        len_list += 1
        curr_node = curr_node.next

    mid = math.floor(len_list / 2)

    i = 0
    curr_node = head
    while i < mid:
        curr_node = curr_node.next
        i += 1
    return curr_node