"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur = root
        
        while cur and cur.left:
            first = cur
            prev = None
            while cur:
                if prev:
                    prev.next = cur.left
                
                cur.left.next = cur.right
                prev = cur.right
                cur = cur.next
            
            cur = first.left
        
        return root