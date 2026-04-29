# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        height = 1
        q = deque([[root, 1]])
        while q:
            node, h = q.popleft()
            height = max(height, h)
            if node.left:
                q.append([node.left, h+1])
            if node.right:
                q.append([node.right, h+1])
        
        res = [[] for _ in range(height)]
        def dfs(node):
            if not node:
                return 0
            
            i = max(dfs(node.left), dfs(node.right))
            res[i].append(node.val)
            return i+1
        
        dfs(root)
        return res