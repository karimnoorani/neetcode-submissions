class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        cache = {}
        def dfs(i, j, edits):
            if i == len(s) and j == len(t):
                return edits == 1
            
            if i == len(s) or j == len(t):
                cache[(i, j, edits)] = dfs(len(s), len(t), edits+len(t)-j+len(s)-i)
                return cache[(i, j, edits)]
            
            if edits > 1:
                return False

            if (i, j, edits) in cache:
                return cache[(i, j, edits)]

            if s[i] == t[j]:
                cache[(i, j, edits)] = dfs(i+1, j+1, edits)
            else:
                cache[(i, j, edits)] = dfs(i+1, j, edits+1) or dfs(i, j+1, edits+1) or dfs(i+1, j+1, edits+1)
            
            return cache[(i, j, edits)]
        
        return dfs(0, 0, 0)