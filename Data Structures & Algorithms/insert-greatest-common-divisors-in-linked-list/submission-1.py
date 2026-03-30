# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        prev = head
        cur = head.next

        while cur:
            new = ListNode(gcd(prev.val, cur.val), cur)
            prev.next = new
            prev, cur = cur, cur.next
        
        return head