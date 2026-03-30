class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val
        self.total -= self.q.popleft() if len(self.q) > self.size else 0
        return self.total / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
