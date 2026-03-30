# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        goodNodes = 0
        def dfs(cur):
            nonlocal goodNodes
            if not cur:
                return
            
            path.append(cur.val)
            if max(path) == cur.val:
                goodNodes += 1
            
            dfs(cur.left)
            dfs(cur.right)
            path.pop()
        
        dfs(root)
        return goodNodes