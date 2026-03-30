class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1

        while target != 0:
            for i in range(target-1, -1, -1):
                if nums[i]+i >= target:
                    target = i
                    break
            
            if i == 0 and target != 0:
                return False
        
        return True
                