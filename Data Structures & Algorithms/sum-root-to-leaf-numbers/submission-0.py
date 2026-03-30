# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        path = []

        def dfs(node):
            path.append(str(node.val))

            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            
            if not node.left and not node.right:
                nonlocal res
                res += int("".join(path))
            
            path.pop()
        
        dfs(root)
        return res