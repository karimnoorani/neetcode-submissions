# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        j = (length-k)%length
        if j == 0:
            return head

        i = 1
        cur = head
        while i < j:
            cur = cur.next
            i += 1
        
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead