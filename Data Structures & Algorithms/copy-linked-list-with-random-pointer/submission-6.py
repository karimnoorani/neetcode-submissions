"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodeMap = {}

        cur = head

        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            nodeMap[cur].next = nodeMap[cur.next] if cur.next != None else None
            nodeMap[cur].random = nodeMap[cur.random] if cur.random != None else None
            cur = cur.next
        
        return nodeMap[head]