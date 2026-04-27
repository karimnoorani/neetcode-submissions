class Solution:

    def __init__(self, weights: List[int]):
        self.total = sum(weights)
        self.ranges = [0]
        for i in range(len(weights)):
            self.ranges.append(self.ranges[-1]+weights[i])

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        L, R = 0, len(self.ranges)-2
        while L <= R:
            M = (L + R) // 2
            if target <= self.ranges[M]:
                R = M - 1
            elif target > self.ranges[M+1]:
                L = M + 1
            else:
                return M


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()