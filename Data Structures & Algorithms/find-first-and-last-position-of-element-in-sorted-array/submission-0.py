class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L, R = 0, len(nums)-1
        right_index = -1
        while L <= R:
            M = (L+R) // 2
            if nums[M] <= target:
                right_index = M if nums[M] == target else right_index
                L = M + 1
            else:
                R = M - 1
        
        if right_index == -1:
            return [-1, -1]
        
        L, R = 0, right_index
        left_index = -1
        while L <= R:
            M = (L+R) // 2
            if nums[M] >= target:
                left_index = M if nums[M] == target else left_index
                R = M - 1
            else:
                L = M + 1
        
        return [left_index, right_index]
