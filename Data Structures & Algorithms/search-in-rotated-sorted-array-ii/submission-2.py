class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums)-1

        while L <= R:
            M = (L+R)//2

            if nums[M] == target:
                return True
            
            if nums[M] > nums[L]: # Left sorted portion
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            elif nums[M] < nums[L]: # Right sorted portion
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            else:
                L += 1
        
        return False