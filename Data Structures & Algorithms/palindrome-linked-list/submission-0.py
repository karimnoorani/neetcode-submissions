# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        sP = fP = head
        while fP and fP.next:
            sP = sP.next
            fP = fP.next.next
        
        prev = None
        while sP:
            tmp = sP.next
            sP.next = prev
            prev = sP
            sP = tmp
        
        cur = head
        while prev and cur:
            if prev.val != cur.val:
                return False
            prev = prev.next
            cur = cur.next
        
        return True