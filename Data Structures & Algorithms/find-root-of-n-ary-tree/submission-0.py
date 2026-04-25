"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        adjList = defaultdict(list)
        
        for parent in tree:
            for child in parent.children:
                adjList[child].append(parent)
        
        for node in tree:
            if len(adjList[node]) == 0:
                return node