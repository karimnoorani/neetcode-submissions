class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxHeap = []
        self.count = 0
        self.valid = set()

    def cleanMaxHeap(self):
        while self.maxHeap[0][1] not in self.valid:
            heapq.heappop(self.maxHeap)
        
    def cleanStack(self):
        while self.stack[-1][1] not in self.valid:
            self.stack.pop()

    def push(self, x: int) -> None:
        heapq.heappush(self.maxHeap, [-x, self.count])
        self.valid.add(self.count)
        self.stack.append([x, self.count])
        self.count -= 1

    def pop(self) -> int:
        self.cleanStack()
        x, count = self.stack.pop()
        self.valid.remove(count)
        return x

    def top(self) -> int:
        self.cleanStack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self.cleanMaxHeap()
        return -self.maxHeap[0][0]

    def popMax(self) -> int:
        self.cleanMaxHeap()
        x, count = heapq.heappop(self.maxHeap)
        self.valid.remove(count)
        return -x


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
