# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(2000)

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = 0
        self.arr = self.getLOT(root)
    
    def getLOT(self, node):
        if not node:
            return []
        
        return self.getLOT(node.left) + [node.val] + self.getLOT(node.right)

    def next(self) -> int:
        res = self.arr[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < len(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()