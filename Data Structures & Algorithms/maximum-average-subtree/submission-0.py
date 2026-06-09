# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxValue = 0

        def dfs(node):
            if not node:
                return [0, 0]
            
            nonlocal maxValue
            leftTotal, leftCount = dfs(node.left)
            rightTotal, rightCount = dfs(node.right)

            maxValue = max(maxValue, (leftTotal+rightTotal+node.val)/(leftCount+rightCount+1))
            return [leftTotal+rightTotal+node.val, leftCount+rightCount+1]
        
        dfs(root)
        return maxValue