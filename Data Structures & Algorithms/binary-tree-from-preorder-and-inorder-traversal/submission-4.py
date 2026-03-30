# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return
            
            node = TreeNode(preorder[self.preIdx])
            left = idx[preorder[self.preIdx]]
            self.preIdx += 1
            node.left = dfs(l, left - 1)
            node.right = dfs(left + 1, r)

            return node
        
        return dfs(0, len(inorder)-1)