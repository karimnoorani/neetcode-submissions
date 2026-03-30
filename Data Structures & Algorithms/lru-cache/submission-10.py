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

    def get(self, key: int) -> int:
        if key in self.keyMap:
            node = self.keyMap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next, node.prev = self.right, self.right.prev
            self.right.prev.next = node
            self.right.prev = node
            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = [key, value]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next, node.prev = self.right, self.right.prev
            self.right.prev.next = node
            self.right.prev = node
        else:
            new = ListNode([key, value], self.right, self.right.prev)
            self.right.prev.next = new
            self.right.prev = new
            self.keyMap[key] = new
            if self.space - 1 < 0:
                del self.keyMap[self.left.next.val[0]]
                self.left.next = self.left.next.next
                self.left.next.prev = self.left
                self.space += 1
            self.space -= 1
