# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            heapq.heappush(heap, [-abs(target-node.val), node.val])
            if len(heap) > k:
                heapq.heappop(heap)
            dfs(node.right)
        
        dfs(root)
        return [x[1] for x in heap]