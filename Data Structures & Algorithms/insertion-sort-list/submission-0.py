# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insert(node, head):
            if not head or node.val < head.val:
                node.next = head
                return node
            
            prev = head
            cur = head.next
            while cur and cur.val < node.val:
                prev = cur
                cur = cur.next
            
            prev.next, node.next = node, cur
            return head
        
        res = None
        while head:
            tmp = head.next
            res = insert(head, res)
            head = tmp
        
        return res