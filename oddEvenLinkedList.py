# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return head
    if not head.next:
        return head

    oddHead, evenHead = head, head.next
    curr, nxt = head, head.next
    lastOdd = oddHead
    odd = True
    while nxt:
        if odd and nxt.next:
            lastOdd = nxt.next
        curr.next = nxt.next
        curr = nxt
        nxt = nxt.next
        odd = not odd
    lastOdd.next = evenHead
    return oddHead