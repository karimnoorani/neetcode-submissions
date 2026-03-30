# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if not root.right and val > root.val:
            root.right = TreeNode(val)
        
        elif not root.left and val < root.val:
            root.left = TreeNode(val)
        
        else:
            self.insertIntoBST(root.right if val > root.val else root.left, val)
        
        return root