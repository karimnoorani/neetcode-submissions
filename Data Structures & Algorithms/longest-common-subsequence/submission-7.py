class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        cache = {}
        def dfs(i, j):
            if i >= len(s1) or j >= len(s2):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s1[i] == s2[j]:
                cache[(i, j)] = 1+dfs(i+1, j+1)
            else:
                cache[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            
            return cache[(i, j)]
        
        return dfs(0, 0)