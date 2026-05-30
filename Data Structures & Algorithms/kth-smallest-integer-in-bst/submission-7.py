# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k

        def dfs(node):
            if not node:
                return None
            
            nonlocal cnt
            left = dfs(node.left)
            if left is not None:
                return left
            
            if cnt == 1:
                return node.val
            
            cnt -=1
            return dfs(node.right)
        
        return dfs(root)