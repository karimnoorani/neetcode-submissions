class ListNode:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = ListNode()
        self.right = ListNode()
        self.capacity = capacity

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        print(f"Removing {node.val}")
        node.prev.next, node.next.prev = node.next, node.prev
        self.capacity += 1
    
    def insert(self, key, val):
        print(f"Inserting {key}, {val}")
        node = ListNode([key, val], self.right.prev, self.right)
        self.right.prev.next, self.right.prev = node, node
        if self.capacity == 0:
            del self.cache[self.left.next.val[0]]
            self.remove(self.left.next)
        self.capacity -= 1
        return node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        res = self.cache[key].val
        self.remove(self.cache[key])
        newPtr = self.insert(res[0], res[1])
        self.cache[key] = newPtr
        return res[1]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = self.insert(key, value)
