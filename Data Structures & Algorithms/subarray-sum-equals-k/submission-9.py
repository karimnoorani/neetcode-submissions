class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_prefixes = defaultdict(int)
        prev_prefixes[0] = 1
        prefix = 0
        subarrays = 0

        for num in nums:
            prefix += num
            subarrays += prev_prefixes[prefix-k]
            prev_prefixes[prefix] += 1
        
        return subarrays
