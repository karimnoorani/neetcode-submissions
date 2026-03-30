class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        targetSide = sum(matchsticks)//4
        def dfs(left, top, right, down, i):
            if i == len(matchsticks):
                if left == top == right == down:
                    return True
                else:
                    return False
            
            if max(left, top, right, down) > targetSide:
                return False
            
            addLeft = dfs(left+matchsticks[i], top, right, down, i+1)
            addTop = dfs(left, top+matchsticks[i], right, down, i+1)
            addRight = dfs(left, top, right+matchsticks[i], down, i+1)
            addDown = dfs(left, top, right, down+matchsticks[i], i+1)

            return addLeft or addTop or addRight or addDown
        
        return dfs(0, 0, 0, 0, 0)