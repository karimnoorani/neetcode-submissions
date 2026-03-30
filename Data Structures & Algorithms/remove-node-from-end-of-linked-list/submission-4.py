# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # Get length of list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        # Get nFromStart (0-index)
        nFromStart = length - n

        # Handle base case
        if nFromStart == 0:
            return head.next
        
        # Get to prev node
        cur = head
        i = 1
        while i < nFromStart:
            cur = cur.next
            i += 1
        
        print(cur.val)
        # Remove the node from list
        cur.next = cur.next.next

        return head