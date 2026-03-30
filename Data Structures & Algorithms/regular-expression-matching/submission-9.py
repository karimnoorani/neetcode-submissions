class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            print(i, j)
            if i == len(s) and j == len(p):
                return True
            
            if j == len(p):
                return False
            
            if i == len(s):
                if p[j] == '*':
                    cache[(i, j)] = dfs(i, j+1)
                elif j + 1 < len(p) and p[j+1] == '*':
                    cache[(i, j)] = dfs(i, j+2)
                else:
                    cache[(i, j)] = False
                return cache[(i, j)]
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == p[j] or p[j] == '.':
                cache[(i, j)] = dfs(i+1, j+1)
                if j + 1 < len(p) and p[j+1] == '*':
                    cache[(i, j)] = cache[(i, j)] or dfs(i, j+2)
            elif p[j] == '*':
                if j > 0 and (s[i] == p[j-1] or p[j-1] == '.'):
                    cache[(i, j)] = dfs(i+1, j+1) or dfs(i+1, j) or dfs(i, j+1)
                else:
                    cache[(i, j)] = dfs(i, j+1)
            elif j + 1 < len(p) and p[j+1] == '*':
                cache[(i, j)] = dfs(i, j+2)
            else:
                cache[(i, j)] = False
            
            return cache[(i, j)]
        
        return dfs(0, 0)