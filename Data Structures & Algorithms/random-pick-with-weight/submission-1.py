import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.ranges = []
        self.maxInt = sum(w)-1
        prev = -1
        for weight in w:
            self.ranges.append(prev+weight)
            prev = prev+weight

    def pickIndex(self) -> int:
        num = random.randint(0, self.maxInt)
        return bisect.bisect_left(self.ranges, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()