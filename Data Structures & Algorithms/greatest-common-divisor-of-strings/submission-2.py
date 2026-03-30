class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def dfs(s, t):
            if len(s) == 0:
                return True
            
            if len(s) < len(t) or s[:len(t)] != t:
                return False

            return dfs(s[len(t):], t)
        
        res = ""
        for i in range(1, len(str2)+1):
            if dfs(str1, str2[:i]) and dfs(str2, str2[:i]):
                res = str2[:i]
        
        return res