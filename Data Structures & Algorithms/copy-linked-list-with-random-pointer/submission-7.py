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
        nodeMap = {}

        def dfs(node):
            if not node:
                return None
            
            if node in nodeMap:
                return nodeMap[node]

            nodeMap[node] = Node(node.val)
            nodeMap[node].next = dfs(node.next)
            nodeMap[node].random = dfs(node.random)

            return nodeMap[node]
        
        return dfs(head)