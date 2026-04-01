# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        indexMap = {}
        
        i = 0
        cur = head
        while cur:
            indexMap[i] = cur.val
            i += 1
            cur = cur.next
        
        cur = head
        length = i
        i = 0
        while cur:
            cur.val = indexMap[(i-k)%length]
            i += 1
            cur = cur.next
        
        return head