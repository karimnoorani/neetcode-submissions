# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        length, cur = 0, head

        while cur:
            length += 1
            cur = cur.next
        
        nFromStart = length - n + 1
        i = 1
        cur = head
        
        if nFromStart == 1:
            return head.next
        
        while i + 1 < nFromStart:
            i += 1
            cur = cur.next
        
        cur.next = cur.next.next
        return head
        