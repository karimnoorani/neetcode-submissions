# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        while l1 or l2:
            if l1:
                s1 = str(l1.val) + s1
                l1 = l1.next
            if l2:
                s2 = str(l2.val) + s2
                l2 = l2.next
        
        total = list(str(int(s1) + int(s2)))[::-1]
        curr = head = ListNode()

        for val in total:
            curr.next = ListNode(val)
            curr = curr.next
        
        return head.next