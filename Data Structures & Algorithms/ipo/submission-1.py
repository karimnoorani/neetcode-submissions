import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        selected = []
        currentW = w
        while len(selected) < k:
            maxHeap = []
            i = 0
            for p, c in zip(profits, capital):
                if currentW >= c and i not in selected:
                    maxHeap.append([-p, i])
                i += 1
            if len(maxHeap) == 0:
                return currentW
            heapq.heapify(maxHeap)
            p, i = heapq.heappop(maxHeap)

            currentW += -p
            selected.append(i)
        
        return currentW
