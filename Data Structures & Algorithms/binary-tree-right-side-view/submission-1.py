# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            qLen = len(q)
            rightSide = None
            for _ in range(qLen):
                node = q.popleft()
                if node is None:
                    continue
                if not rightSide:
                    rightSide = node.val
                q.append(node.right)
                q.append(node.left)
            if rightSide:
                res.append(rightSide)
        
        return res