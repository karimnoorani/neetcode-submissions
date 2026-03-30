# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            
            nonlocal res
            print(root.val, res)
            maxLeft = dfs(root.left)
            maxRight = dfs(root.right)

            res = max(res, maxLeft + maxRight)

            return 1 + max(maxLeft, maxRight)
        
        dfs(root)

        return res