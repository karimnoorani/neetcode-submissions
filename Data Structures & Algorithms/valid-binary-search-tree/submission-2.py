# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node, minVal, maxVal):
            if node is None:
                return
            
            if node.val >= maxVal or node.val <= minVal:
                nonlocal res
                res = False
                return
            
            dfs(node.left, minVal, min(maxVal, node.val))
            dfs(node.right, max(minVal, node.val), maxVal)
        
        dfs(root, float('-inf'), float('inf'))
        return res