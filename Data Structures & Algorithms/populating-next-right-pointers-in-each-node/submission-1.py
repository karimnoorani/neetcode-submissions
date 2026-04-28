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
        if not root:
            return root
        level = deque([root])
        while level:
            next_level = deque()
            while level:
                node = level.popleft()
                if level:
                    node.next = level[0]
                
                if node.left and node.right:
                    next_level.append(node.left)
                    next_level.append(node.right)
            level = next_level
        return root