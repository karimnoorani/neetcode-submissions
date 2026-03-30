class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        intervals = deque(intervals)
        minHeap = []
        res = [-1 for _ in range(len(queries))]
        queries = [[q, i] for i, q in enumerate(queries)]

        for q, i in sorted(queries):
            while intervals and q >= intervals[0][0]:
                l, r = intervals.popleft()
                heapq.heappush(minHeap, [r-l+1, r])
            
            while minHeap and q > minHeap[0][1]:
                heapq.heappop(minHeap)
            
            res[i] = minHeap[0][0] if minHeap else -1
        
        return res
