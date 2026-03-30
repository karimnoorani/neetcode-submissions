"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            
            nodeMap[node] = Node(node.val)
            neighbors = []
            for nei in node.neighbors:
                neighbors.append(dfs(nei))
            
            nodeMap[node].neighbors = neighbors
            return nodeMap[node]
        
        return dfs(node)