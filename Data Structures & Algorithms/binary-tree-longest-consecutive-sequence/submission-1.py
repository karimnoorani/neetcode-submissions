# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 1
        def dfs(node):
            if not node:
                return 0
            
            left_seq_length = dfs(node.left)
            right_seq_length = dfs(node.right)

            if node.left and node.val + 1 == node.left.val:
                left_seq_length = left_seq_length
            else:
                left_seq_length = 0
            
            if node.right and node.val + 1 == node.right.val:
                right_seq_length = right_seq_length
            else:
                right_seq_length = 0
            
            nonlocal res
            res = max(res, 1+max(left_seq_length, right_seq_length))
            return 1+max(left_seq_length, right_seq_length)
        
        dfs(root)
        return res