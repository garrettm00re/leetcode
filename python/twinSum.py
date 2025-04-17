# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        n = len(arr)
        mSum = 0
        
        for i in range(n/2):
            el, twinEl = arr[i], arr[-1 * (i + 1)]
            mSum = max(mSum, el + twinEl)
        return mSum