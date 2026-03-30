# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visited = set()
        
        while stack:
            cur = stack.pop()
            
            if cur is None:
                continue
            
            if cur in visited:
                res.append(cur.val)
                continue
            
            stack.append(cur)
            visited.add(cur)
            stack.append(cur.right)
            stack.append(cur.left)
        
        return res
