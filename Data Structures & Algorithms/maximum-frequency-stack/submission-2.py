class FreqStack:
    def __init__(self):
        self.freqToNums = defaultdict(list)
        self.numToFreq = defaultdict(int)
        self.mostFreqCnt = 0

    def push(self, val: int) -> None:
        self.numToFreq[val] += 1
        self.freqToNums[self.numToFreq[val]].append(val)
        self.mostFreqCnt = max(self.mostFreqCnt, self.numToFreq[val])

    def pop(self) -> int:
        res = self.freqToNums[self.mostFreqCnt].pop()
        self.numToFreq[res] -= 1
        if len(self.freqToNums[self.mostFreqCnt]) == 0:
            self.mostFreqCnt -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()