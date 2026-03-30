# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        indexMap = {}
        while head:
            indexMap[n] = head.val
            head = head.next
            n += 1
        
        res = 0
        for i in range(n//2):
            res = max(res, indexMap[i]+indexMap[n-i-1])
        
        return res