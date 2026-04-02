# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cur1, cur2 = l1, l2
        
        while cur1 or cur2:
            if cur1:
                num1 = num1*10+cur1.val
                cur1 = cur1.next
            if cur2:
                num2 = num2*10+cur2.val
                cur2 = cur2.next
        
        total = num1+num2
        cur = None
        if total == 0:
            return ListNode()
        while total > 0:
            tmp = ListNode(total%10, cur)
            total = total // 10
            cur = tmp
        
        return cur