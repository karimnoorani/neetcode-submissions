# [1, 1, 2, 2, 3]
#  L           R
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        
        while L <= R:
            M = (L+R) // 2
            M = M - 1 if M % 2 == 1 else M

            if M > 0 and nums[M] == nums[M-1]:
                R = M - 2
            elif M < len(nums)-1 and nums[M] == nums[M+1]:
                L = M + 2
            else:
                return nums[M]