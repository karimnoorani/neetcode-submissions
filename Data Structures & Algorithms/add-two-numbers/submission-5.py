# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []

        while l1 or l2:
            if l1:
                nums1.append(str(l1.val))
                l1 = l1.next
            if l2:
                nums2.append(str(l2.val))
                l2 = l2.next
        
        total = str(int("".join(nums1[::-1])) + int("".join(nums2[::-1])))[::-1]

        head = cur = ListNode(int(total[0]))

        for c in total[1:]:
            cur.next = ListNode(int(c))
            cur = cur.next
        
        return head

