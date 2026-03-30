class Solution:
    def jump(self, nums: List[int]) -> int:
        L = R = 0
        jumps = 0
        
        while L <= R:
            farthest = R
            
            if farthest >= len(nums)-1:
                return jumps

            for i in range(L, R+1):
                farthest = max(farthest, i+nums[i])

            L = R+1
            R = farthest
            jumps += 1