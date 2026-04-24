# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        cur = root
        res = root.val

        while cur:
            res = cur.val if abs(cur.val-target) < abs(res-target) else res
            
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
        
        return res