"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()

        while p or q:
            if p == q:
                return p
            
            if p in seen:
                return p
            
            if q in seen:
                return q
            
            if p:
                seen.add(p)
                p = p.parent
            
            if q:
                seen.add(q)
                q = q.parent
        