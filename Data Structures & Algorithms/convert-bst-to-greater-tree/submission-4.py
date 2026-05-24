# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(2000)
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        preorder = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            preorder.append(node.val)
            dfs(node.right)
        
        dfs(root)
        postfix = 0
        sumDict = {}
        for i in range(len(preorder)-1, -1, -1):
            sumDict[preorder[i]] = postfix
            postfix += preorder[i]
        
        def fillValues(node):
            if not node:
                return
            
            node.val += sumDict[node.val]
            fillValues(node.left)
            fillValues(node.right)
        
        fillValues(root)
        return root