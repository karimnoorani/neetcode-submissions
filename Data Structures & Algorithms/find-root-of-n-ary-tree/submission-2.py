"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total = 0
        for parent in tree:
            total += parent.val
            for child in parent.children:
                total -= child.val
        
        for node in tree:
            if node.val == total:
                return node
        
