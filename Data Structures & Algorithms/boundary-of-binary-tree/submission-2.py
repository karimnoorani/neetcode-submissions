# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def isLeaf(node):
            return not node.left and not node.right
        
        def addLeaves(node):
            if node is None:
                return
            
            if isLeaf(node):
                res.append(node.val)
                return
            
            if node.left:
                addLeaves(node.left)
            
            if node.right:
                addLeaves(node.right)
        
        res.append(root.val)
        cur = root.left
        while cur:
            if not isLeaf(cur):
                res.append(cur.val)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        addLeaves(root.left)
        addLeaves(root.right)

        cur = root.right
        stack = []
        while cur:
            if not isLeaf(cur):
                stack.append(cur.val)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        
        res += stack[::-1]
        return res