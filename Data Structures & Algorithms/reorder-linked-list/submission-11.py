# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sP, fP = head, head.next

        # Running list through list using fast and slow pointers
        while fP and fP.next:
            sP = sP.next
            fP = fP.next.next

        # Getting second half of list and breaking link
        second = sP.next
        prev = sP.next = None

        # Reversing the second half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Insert nodes from list2 into list1
        first, second = head, prev
        while second:
            tmp = first.next
            first.next = second
            second = second.next
            first.next.next = tmp
            first = tmp