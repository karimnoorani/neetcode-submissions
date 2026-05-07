class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefixes[0] = 1
        total = 0
        res = 0

        for n in nums:
            total += n
            res += prefixes[total-k]
            prefixes[total] += 1
        
        return res