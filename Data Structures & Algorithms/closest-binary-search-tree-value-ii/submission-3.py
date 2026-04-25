# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        vals = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        
        dfs(root)
        if len(vals) <= k:
            return vals
        
        res = collections.deque()
        for val in vals:
            if len(res) < k:
                res.append(val)
            else:
                if abs(val - target) < abs(res[0] - target):
                    res.popleft()
                    res.append(val)
                else:
                    break
        return list(res)