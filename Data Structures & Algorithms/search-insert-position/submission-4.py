class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            if R == L:
                if nums[L] < target:
                    return R + 1
                elif nums[R] < target:
                    return L+1
                else:
                    return L
            
            M = (L+R) // 2

            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                return M
        
        return L