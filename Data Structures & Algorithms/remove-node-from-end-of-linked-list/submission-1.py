# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Get nFromStart (accounts for 0th index)
        nFromStart = length-n

        # Remove that element
        prev, curr = None, head
        
        if nFromStart == 0:
            return curr.next
        
        index = 0
        while index != nFromStart:
            prev = curr
            curr = curr.next
            index += 1
        
        prev.next = curr.next
        return head