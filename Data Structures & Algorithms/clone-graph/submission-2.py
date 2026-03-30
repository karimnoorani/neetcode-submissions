"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # Val -> node
        nodeMap = {}
        def createNode(node):
            newNode = Node(node.val)
            nodeMap[newNode.val] = newNode
            for neighbor in node.neighbors:
                if neighbor.val not in nodeMap:
                    createNode(neighbor)
                newNode.neighbors.append(nodeMap[neighbor.val])
            return newNode
        return createNode(node)