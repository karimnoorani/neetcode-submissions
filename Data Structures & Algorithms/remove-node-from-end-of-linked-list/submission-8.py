# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        i = 0

        while r:
            if i > n:
                l = l.next
            r = r.next
            i += 1

        if i <= n:
            return head.next
        
        l.next = l.next.next
        return head
        