class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxTotal):
            arrNum = 1
            currTotal = 0
            for n in nums:
                if currTotal + n > maxTotal:
                    arrNum += 1
                    currTotal = 0
                currTotal += n
            return arrNum <= k

        L, R = max(nums), sum(nums)
        res = R

        while L <= R:
            M = (L+R)//2

            if canSplit(M):
                res = M
                R = M - 1
            else:
                L = M + 1
        
        return res
