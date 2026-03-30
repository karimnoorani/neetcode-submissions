# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def dfs(root):
            if root is None or len(stack) == k:
                return
            
            dfs(root.left)
            if len(stack) < k: stack.append(root.val)
            dfs(root.right)
        
        dfs(root)

        return stack[-1]