import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.small and num < -self.small[0]:
            heapq.heappush(self.small, -num)
        
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large)+1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small)+1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] + -self.small[0])/2
        
        