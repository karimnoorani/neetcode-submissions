class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(i):
            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            if i in cache:
                return cache[i]

            if i < len(s)-1 and int(s[i:i+2]) < 27:
                cache[i] = dfs(i+1) + dfs(i+2)
            else:
                cache[i] = dfs(i+1)
            
            return cache[i]
        
        return dfs(0)


