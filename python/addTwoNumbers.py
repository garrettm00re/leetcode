class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    def constructLinkedList(num):
        if num == 0:
            return ListNode()
        head = None
        while num > 0:
            dig = num % 10
            if not head:
                head = ListNode(val = dig)
                curr = head
            else:
                curr.next = ListNode(val = dig)
                curr = curr.next
            num //= 10
        return head

    place = 1
    n1, n2 = 0, 0
    while (l1 or l2):
        if l1 != None:
            n1 += (l1.val * place)
            l1 = l1.next
        if l2 != None:
            n2 += (l2.val * place)
            l2 = l2.next
        place *= 10
    print(n1 + n2)
    return constructLinkedList(n1 + n2)