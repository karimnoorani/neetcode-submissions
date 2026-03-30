class FreqStack:
    def __init__(self):
        self.maxCnt = 0
        self.cntMap = defaultdict(int)
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.cntMap[val] += 1
        if self.cntMap[val] > self.maxCnt:
            self.maxCnt = self.cntMap[val]
        self.stacks[self.cntMap[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cntMap[res] -= 1
        if len(self.stacks[self.maxCnt]) == 0:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()