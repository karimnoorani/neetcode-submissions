class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.max_heap = []
        self.length = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.length += 1
        heapq.heappush(self.max_heap, [-self.frequency[val], -self.length, val])

    def pop(self) -> int:
        while self.frequency[self.max_heap[0][2]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        _, _, val = heapq.heappop(self.max_heap)
        self.frequency[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()