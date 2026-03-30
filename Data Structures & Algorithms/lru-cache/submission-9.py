class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.store:
            self.store.move_to_end(key, last=False)
            return self.store[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.store) == self.cap and key not in self.store:
            print(self.store.popitem())
        self.store[key] = value
        self.store.move_to_end(key, last=False)
