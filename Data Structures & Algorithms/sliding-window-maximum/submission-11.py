class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # [val, i]
        res = []

        for i in range(len(nums)):
            while q and nums[i] >= q[-1][0]:
                q.pop()
            
            q.append([nums[i], i])

            while i-q[0][1] >= k:
                q.popleft()
            
            if i >= k-1:
                res.append(q[0][0])
        
        return res