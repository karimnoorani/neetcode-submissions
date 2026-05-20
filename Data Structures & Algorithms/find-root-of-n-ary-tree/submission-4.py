"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        for node in tree:
            for child in node.children:
                child.val = child.val * -1
        
        res = None
        for node in tree:
            if node.val > 0:
                res = node
            else:
                node.val = node.val * -1
        
        return res