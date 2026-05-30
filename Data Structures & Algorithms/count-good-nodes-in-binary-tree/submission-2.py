# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, parentMax):
            if not node:
                return 0
            
            left = dfs(node.left, max(node.val, parentMax))
            right = dfs(node.right, max(node.val, parentMax))

            goodNodes = 1+left+right if node.val >= parentMax else left+right
            return goodNodes
        
        return dfs(root, float('-inf'))

                