class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for index, num in enumerate(nums):
            while queue and num >= queue[-1][0]:
                queue.pop()
            
            queue.append([num, index])

            while queue and queue[0][1] < index+1-k:
                queue.popleft()
            
            if index >= k-1:
                result.append(queue[0][0])
        
        return result