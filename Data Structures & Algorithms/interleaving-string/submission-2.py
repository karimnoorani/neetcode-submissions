class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def dfs(p1, p2):
            if p1 == len(s1) and p2 == len(s2):
                return True
            
            if (p1, p2) in cache:
                return cache[(p1, p2)]

            p3 = p1 + p2
            s1c = s1[p1] if p1 < len(s1) else '*'
            s2c = s2[p2] if p2 < len(s2) else '*'
            s3c = s3[p3]

            if s1c == s3c and s2c == s3c:
                cache[(p1, p2)] = dfs(p1+1, p2) or dfs(p1, p2+1)
            elif s1c == s3c:
                cache[(p1, p2)] = dfs(p1+1, p2)
            elif s2c == s3c:
                cache[(p1, p2)] = dfs(p1, p2+1)
            else:
                cache[(p1, p2)] = False
            
            return cache[(p1, p2)]
        
        return dfs(0, 0)