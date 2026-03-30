from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.store = OrderedDict()
        self.remaining_size = capacity

    def get(self, key: int) -> int:
        if key in self.store:
            self.store.move_to_end(key, last=True)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.move_to_end(key, last=True)
            self.store[key] = value
        else:
            if self.remaining_size == 0:
                self.store.popitem(last=False)
            self.store[key] = value
            if self.remaining_size != 0:
                self.remaining_size -= 1
        