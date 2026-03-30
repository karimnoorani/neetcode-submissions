# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(node):
            if not node:
                return 0
            
            nonlocal isBalanced

            leftTree = dfs(node.left)
            rightTree = dfs(node.right)
            isBalanced = isBalanced and abs(leftTree - rightTree) < 2

            return 1 + max(leftTree, rightTree)
        
        dfs(root)

        return isBalanced