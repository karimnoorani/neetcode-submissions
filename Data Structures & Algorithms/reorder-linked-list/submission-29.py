# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 0, 1, 2, 3, 4, 5, 6

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        
        sP = fP = head

        while fP and fP.next:
            sP = sP.next
            fP = fP.next.next
        
        cur = sP.next
        sP.next = None
        prev = None
        
        while cur:
            tmp, cur.next = cur.next, prev
            prev, cur = cur, tmp
        
        list1 = head
        list2 = prev

        while list1 and list2:
            tmp, list1.next = list1.next, list2
            tmp2, list2.next = list2.next, tmp
            list1, list2 = tmp, tmp2
        
        

        
