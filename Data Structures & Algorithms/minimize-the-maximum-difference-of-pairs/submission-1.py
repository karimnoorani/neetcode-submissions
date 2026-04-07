class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def isValid(M):
            res = 0
            i = 0
            while i < len(nums)-1:
                if nums[i+1]-nums[i] <= M:
                    res += 1
                    i += 2
                else:
                    i += 1
            return res >= p
        L, R = 0, nums[-1]-nums[0]
        res = float('inf')

        while L <= R:
            M = (L+R) // 2

            if isValid(M):
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res

            