# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        res = 0
        
        def dfs(node, parent):
            if not node:
                return [True, parent.val]
            
            leftBool, leftVal = dfs(node.left, node)
            rightBool, rightVal = dfs(node.right, node)
            isUnival = leftBool and rightBool and leftVal == node.val == rightVal
            
            if isUnival:
                nonlocal res
                res += 1
            
            return [isUnival, node.val]
        
        dfs(root, None)
        return res

