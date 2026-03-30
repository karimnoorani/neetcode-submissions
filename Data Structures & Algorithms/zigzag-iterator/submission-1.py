class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.indexes = defaultdict(int)
        self.i = 0

    def next(self) -> int:
        while self.indexes[self.i] == len(self.vectors[self.i]):
            self.i = self.i + 1 if self.i + 1 < len(self.vectors) else 0
        res = self.vectors[self.i][self.indexes[self.i]]
        self.indexes[self.i] += 1
        self.i = self.i + 1 if self.i + 1 < len(self.vectors) else 0
        return res

    def hasNext(self) -> bool:
        for i in range(len(self.vectors)):
            if self.indexes[i] < len(self.vectors[i]):
                return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
