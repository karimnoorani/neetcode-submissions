class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def applyQuadratic(n):
            return (a*(n**2))+(b*n)+c

        L, R = 0, len(nums)-1
        res = []
        while L <= R:
            if applyQuadratic(nums[L]) < applyQuadratic(nums[R]):
                if a < 0:
                    res.append(applyQuadratic(nums[L]))
                    L += 1
                else:
                    res.append(applyQuadratic(nums[R]))
                    R -= 1
            else:
                if a < 0:
                    res.append(applyQuadratic(nums[R]))
                    R -= 1
                else:
                    res.append(applyQuadratic(nums[L]))
                    L += 1
        
        return res if a < 0 else res[::-1]
