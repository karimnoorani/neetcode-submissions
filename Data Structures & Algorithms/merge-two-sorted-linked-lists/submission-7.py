# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()

        l1, l2 = list1, list2

        while l1 or l2:
            if not l1 or not l2:
                cur.next = l2 if not l1 else l1
                break
            
            cur.next = l1 if l1.val < l2.val else l2
            cur = cur.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        
        return dummy.next