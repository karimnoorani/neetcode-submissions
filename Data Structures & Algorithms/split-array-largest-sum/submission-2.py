class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxSize):
            buckets = 1
            current_bucket = 0
            for num in nums:
                if current_bucket + num > maxSize:
                    buckets += 1
                    current_bucket = 0
                current_bucket += num
            return buckets <= k
        
        lower_bound, upper_bound = max(nums), sum(nums)
        result = upper_bound
        while lower_bound <= upper_bound:
            middle = (lower_bound + upper_bound) // 2
            
            if canSplit(middle):
                upper_bound = middle - 1
                result = middle
            else:
                lower_bound = middle + 1
        
        return result