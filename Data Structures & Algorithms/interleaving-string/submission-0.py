class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        
        cache = {}
        def dfs(i, j):
            if i >= len(s1) and j >= len(s2):
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s1):
                if s2[j] != s3[i+j]:
                    cache[(i, j)] = False
                    return cache[(i, j)]
                cache[(i, j)] = dfs(i, j+1)
                return cache[(i, j)]
            
            if j >= len(s2):
                if s1[i] != s3[i+j]:
                    cache[(i, j)] = False
                    return cache[(i, j)]
                cache[(i, j)] = dfs(i+1, j)
                return cache[(i, j)]
            
            if s1[i] == s2[j] == s3[i+j]:
                cache[(i, j)] = dfs(i+1, j) or dfs(i, j+1)
                return cache[(i, j)]
            
            if s1[i] == s3[i+j]:
                cache[(i, j)] = dfs(i+1, j)
                return cache[(i, j)]
            
            if s2[j] == s3[i+j]:
                cache[(i, j)] = dfs(i, j+1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)