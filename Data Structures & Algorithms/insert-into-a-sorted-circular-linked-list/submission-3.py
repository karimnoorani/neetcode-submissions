# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        if head == head.next:
            head.next = Node(insertVal, head)
            return head

        cur = head.next
        prev = head

        while True:
            if insertVal >= prev.val and insertVal <= cur.val:
                break
            
            if prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    break
            
            prev = cur
            cur = cur.next
            if prev == head:
                break
        
        prev.next = Node(insertVal, cur)
        return head
