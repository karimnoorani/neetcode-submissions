import sys
sys.setrecursionlimit(3000)

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        cache = {}
        def dfs(left, right):
            if (left, right) in cache:
                return cache[(left, right)]
            
            while left < right:
                if s[left] != s[right]:
                    cache[(left, right)] = 1+min(dfs(left+1, right), dfs(left, right-1))
                    return cache[(left, right)] 
                
                left += 1
                right -= 1
            
            cache[(left, right)] = 0
            return cache[(left, right)]
        
        return dfs(0, len(s)-1) <= k 