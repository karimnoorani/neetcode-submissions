# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 1

        def dfs(node, parent, length):
            if not node:
                return
            
            length = length + 1 if parent and node.val - 1 == parent.val else 1

            nonlocal res
            res = max(res, length)
            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, None, 0)
        return res
            