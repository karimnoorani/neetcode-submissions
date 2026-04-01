class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        res = []
        minTotal = float('INF')
        path = []
        def dfs(i, total):
            if coins[i] == -1:
                return
           
            path.append(str(i+1))
            total += coins[i]
            print(path)
            if i == len(coins)-1:
                nonlocal minTotal
                nonlocal res
                if total < minTotal or (total == minTotal and "".join(path) < "".join(res)):
                    minTotal = total
                    res = path[:]
            else:
                for j in range(i+1, min(len(coins), i+1+maxJump)):
                    dfs(j, total)
            path.pop()
        
        dfs(0, 0)
        return list(map(int, res))
            
