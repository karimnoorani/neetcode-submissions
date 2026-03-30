# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        newHead = ListNode(0, head)
        def dfs(node):
            carry = dfs(node.next) if node.next else 1
            val = (node.val + carry) % 10
            carry = (node.val + carry) // 10
            node.val = val
            return carry
        
        dfs(newHead)
        return newHead if newHead.val != 0 else newHead.next