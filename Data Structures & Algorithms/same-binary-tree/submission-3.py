# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True
            
            if p and not q:
                return False
            
            if q and not p:
                return False
            
            return p.val == q.val and dfs(p.right, q.right) and dfs(p.left, q.left)
        
        return dfs(p, q)