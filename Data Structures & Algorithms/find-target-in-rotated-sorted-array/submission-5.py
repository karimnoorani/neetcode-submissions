class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            M = (L+R)//2
            print(nums[M])

            if nums[M] == target:
                return M
            
            if nums[M] >= nums[L]:
                if nums[L] <= target < nums[M]:
                    R -= 1
                else:
                    L += 1
            else:
                if nums[M] < target <= nums[R]:
                    L += 1
                else:
                    R -= 1
        
        return -1
            
