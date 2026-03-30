# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, cur = 0, head
        while cur:
            length, cur = length + 1, cur.next
        
        nFromStart = length-n

        if nFromStart == 0:
            return head.next
        
        cur, i = head, 0
        while i+1 < nFromStart:
            i += 1
            cur = cur.next
        
        cur.next = cur.next.next
        return head