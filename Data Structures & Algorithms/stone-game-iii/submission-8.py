import sys
sys.setrecursionlimit(10000)

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}

        def dfs(i):
            if i == len(stoneValue):
                return 0

            if i in cache:
                return cache[i]
            
            res = float('-INF')
            total = 0
            for j in range(3):
                if i + j >= len(stoneValue):
                    break
                total += stoneValue[i+j]
                res = max(res, total-dfs(i+j+1))
            
            cache[i] = res
            return cache[i]
        
        res = dfs(0)
        print(res)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"     
