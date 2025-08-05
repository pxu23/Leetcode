def pairSum(head):
    """
    :type head: Optional[ListNode]
    :rtype: int
    """
    max_twin_sum = 0

    # get the length of list
    n = 0
    cur_node = head
    while cur_node:
        n += 1
        cur_node = cur_node.next

    # get to the second half of the list and reverse

    i = 0
    tail = head
    while i < n / 2 - 1:
        tail = tail.next
        i = i + 1

    # perform the reversal
    cur = tail.next
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    reversed = prev

    # computes the twin sum
    t1 = head
    t2 = reversed
    while t1 and t2:
        cur_twin_sum = t1.val + t2.val
        max_twin_sum = max(max_twin_sum, cur_twin_sum)
        t1 = t1.next
        t2 = t2.next

    return max_twin_sum
