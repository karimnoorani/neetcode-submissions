class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.keyMap = {}
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, None)
        self.left.next, self.right.prev = self.right, self.left
        self.space = capacity
    
    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node) -> None:
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
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
            node = ListNode([key, value], None, None)
            self.insert(node)
            self.keyMap[key] = node
            if self.space < 1:
                first = self.left.next
                self.remove(first)
                del self.keyMap[first.val[0]]
                self.space += 1
            self.space -= 1
