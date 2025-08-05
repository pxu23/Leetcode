def oddEvenList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not head or not head.next:
        return head

    odd = head
    evenHead = head.next
    even = evenHead

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead
    return head