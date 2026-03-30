import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #Initialize two heaps
        maxHeap = []
        minHeap = []
        
        for p, c in zip(profits, capital):
            if w >= c:
                maxHeap.append(-p)
            else:
                minHeap.append([c, p])
        
        heapq.heapify(maxHeap)
        heapq.heapify(minHeap)

        selected = 0
        currentW = w
        while selected < k:
            if len(maxHeap) == 0:
                break
            p = -heapq.heappop(maxHeap)
            currentW += p
            selected += 1
            while minHeap and currentW >= minHeap[0][0]:
                c, p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -p)
        return currentW
            