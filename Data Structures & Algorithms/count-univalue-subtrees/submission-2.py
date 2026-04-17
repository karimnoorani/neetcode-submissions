# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node):
            if not node:
                return True
            
            left, leftVal = dfs(node.left), node.left.val if node.left else node.val
            right, rightVal = dfs(node.right), node.right.val if node.right else node.val
            isUnival = left and right and leftVal == node.val == rightVal
            
            if isUnival:
                nonlocal res
                res += 1
            
            return isUnival
        
        dfs(root)
        return res

