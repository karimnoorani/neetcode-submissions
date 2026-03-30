class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.keyMap = {}
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        self.space = capacity
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.next, node.prev = self.right, self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.keyMap:
            node = self.keyMap[key]
            self.remove(node)
            self.insert(node)
            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = [key, value]
            self.remove(node)
            self.insert(node)
        else:
            new = ListNode([key, value], self.right, self.right.prev)
            self.insert(new)
            self.keyMap[key] = new
            if self.space - 1 < 0:
                del self.keyMap[self.left.next.val[0]]
                self.remove(self.left.next)
                self.space += 1
            self.space -= 1
