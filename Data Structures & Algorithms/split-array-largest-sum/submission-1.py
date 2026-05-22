class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isSumValid(threshold):
            count = 1
            total = 0
            for n in nums:
                if total + n > threshold:
                    count += 1
                    total = 0
                total += n
            return count <= k
        
        lower, upper = max(nums), sum(nums)
        res = upper

        while lower <= upper:
            middle = (lower + upper) // 2

            if isSumValid(middle):
                res = middle
                upper = middle - 1
            else:
                lower = middle + 1
        
        return res