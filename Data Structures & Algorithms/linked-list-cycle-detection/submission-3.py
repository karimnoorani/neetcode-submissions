# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sP, fP = head, head.next

        while fP and fP.next:
            if sP == fP:
                return True
            sP = sP.next
            fP = fP.next.next
        
        return False