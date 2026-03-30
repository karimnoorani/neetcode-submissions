# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head
        if head is None:
            return head
        curr = curr.next
        prev.next = None
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev

            