# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def enoughNodes(node):
            tmp, i = node, 0
            
            while tmp:
                i += 1
                tmp = tmp.next
            
            return i >= k
        
        def reverseKNodes(cur):
            i = 0
            start = cur
            prev = None
            while i < k:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                i += 1
            start.next = cur
            return [prev, cur, start]

        cur = res = head
        first = True

        while enoughNodes(cur):
            if first:
                res, cur, end = reverseKNodes(cur)
                first = False
            else:
                start, cur, newEnd = reverseKNodes(cur)
                end.next = start
                end = newEnd
        
        return res


