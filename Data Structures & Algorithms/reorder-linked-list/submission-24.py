# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        
        sP, fP = head, head.next

        while fP and fP.next:
            sP = sP.next
            fP = fP.next.next
        
        second = sP.next
        prev = sP.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev
        first = head
        
        while second:
            tmp = first.next
            first.next = second
            second = second.next
            first.next.next = tmp
            first = tmp