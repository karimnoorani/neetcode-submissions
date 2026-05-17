# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_incr, left_decr = dfs(node.left)
            right_incr, right_decr = dfs(node.right)

            if node.left:
                left_incr = 0 if node.val + 1 != node.left.val else left_incr
                left_decr = 0 if node.val - 1 != node.left.val else left_decr
            else:
                left_incr, left_decr = 0, 0
            
            if node.right:
                right_incr = 0 if node.val + 1 != node.right.val else right_incr
                right_decr = 0 if node.val - 1 != node.right.val else right_decr
            else:
                right_incr, right_decr = 0, 0
            
            nonlocal res
            res = max(res, 1+left_incr+right_decr, 1+left_decr+right_incr)

            return [1+max(left_incr, right_incr), 1+max(left_decr, right_decr)]
        
        dfs(root)
        return res
