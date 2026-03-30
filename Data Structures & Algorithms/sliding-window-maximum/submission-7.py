import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        maxList = []
        
        for i in range(len(nums)):
            heapq.heappush(heap, [-nums[i], i])
            
            while heap[0][1] < (i-k+1):
                heapq.heappop(heap)
            
            if i >= k-1:
                maxList.append(-heap[0][0])

        return maxList

