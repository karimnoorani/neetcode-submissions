import heapq

class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        
        if (len(self.large)+len(self.small)) % 2 == 0:
            return (self.large[0] + -self.small[0])/2
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        else:
            return -self.small[0]
        