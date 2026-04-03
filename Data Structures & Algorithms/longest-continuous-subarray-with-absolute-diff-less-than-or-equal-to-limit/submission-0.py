class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap = []
        maxHeap = []
        L = 0
        res = 1

        for R in range(len(nums)):
            heapq.heappush(minHeap, [nums[R], R])
            heapq.heappush(maxHeap, [-nums[R], R])

            while abs(minHeap[0][0]+maxHeap[0][0]) > limit:
                if maxHeap[0][1] < minHeap[0][1]:
                    _, i = heapq.heappop(maxHeap)
                else:
                    _, i = heapq.heappop(minHeap)
                L = max(L, i+1)
            
            while L > minHeap[0][1] or L > maxHeap[0][1]:
                if L > minHeap[0][1]:
                    heapq.heappop(minHeap)
                if L > maxHeap[0][1]:
                    heapq.heappop(maxHeap)
            
            res = max(res, R-L+1)
        
        return res
            
