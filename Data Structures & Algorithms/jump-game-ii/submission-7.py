from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        q = deque([0])
        visited = set([0])

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                
                if i >= len(nums)-1:
                    return jumps
                
                for j in range(nums[i], -1, -1):
                    if i+j not in visited:
                        q.append(i+j)
                        visited.add(i+j)
            jumps += 1
        
        raise Exception()
            