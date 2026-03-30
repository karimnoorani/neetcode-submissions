# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        newHead = ListNode(0, head)
        def dfs(node):
            if not node.next:
                val = (node.val + 1) % 10
                carry = (node.val + 1) // 10
                node.val = val
                return carry
            
            carry = dfs(node.next)
            val = (node.val + carry) % 10
            carry = (node.val + carry) // 10
            node.val = val
            return carry
        
        dfs(newHead)
        return newHead if newHead.val != 0 else newHead.next