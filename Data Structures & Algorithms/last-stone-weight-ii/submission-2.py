class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        cache = {}
        target = sum(stones) // 2

        def dfs(i, total):
            if total == target:
                return sum(stones)-total*2
            
            if i == len(stones) or total > target:
                return abs(sum(stones)-total*2)
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = min(dfs(i+1, total+stones[i]), dfs(i+1, total))

            return cache[(i, total)]
        
        return dfs(0, 0)