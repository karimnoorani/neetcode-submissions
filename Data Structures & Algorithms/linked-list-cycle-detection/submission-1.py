# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        sP, fP = head, head.next

        while fP and fP.next:
            if fP == sP:
                return True
            else:
                fP = fP.next.next
                sP = sP.next
        
        return False