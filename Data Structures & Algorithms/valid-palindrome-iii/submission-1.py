class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        cache = {}
        def dfs(left, right, k):
            if k < 0:
                return False
            if (left, right, k) in cache:
                return cache[(left, right, k)]
            
            while left < right:
                if s[left] != s[right]:
                    cache[(left, right, k)] = dfs(left+1, right, k-1) or dfs(left, right-1, k-1)
                    return cache[(left, right, k)] 
                
                left += 1
                right -= 1
            
            cache[(left, right, k)] = True
            return cache[(left, right, k)]
        
        return dfs(0, len(s)-1, k)