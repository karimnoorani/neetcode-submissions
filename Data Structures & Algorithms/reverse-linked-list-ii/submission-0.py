# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# i = 3
#  0 -> 1 -> 2 ->  3  -> 4 -> 5 -> 6 -> 7
#      lP   prev  cur
#  0 -> 1    5->  4 ->  3  -> 2 
#.          curr prev
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head
        
        lP = None
        curr = head
        i = 1

        while i < left:
            i += 1
            lP = curr
            curr = curr.next
        
        prev = None
        start = curr
        while i <= right:
            i += 1
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        start.next = curr
        if lP is not None:
            lP.next = prev
            return head
        else:
            return prev

                