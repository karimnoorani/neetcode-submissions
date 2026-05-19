import sys

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = {}
        freq = Counter(nums)
        res = 0

        def dfs(num):
            if num == 1:
                return float('inf')
            
            if num == 2:
                return 1

            if num == 0:
                return 0
            
            if num % 3 == 0:
                return num // 3
            
            if num in cache:
                return cache[(num)]
            
            cache[(num)] = 1+min(dfs(num-2), dfs(num-3))
            return cache[(num)]
        
        for num in freq:
            ops = dfs(freq[num])
            
            if ops == float('inf'):
                return -1
            
            res += ops

        return res