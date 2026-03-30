class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitMap = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7":["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        cache = {}
        def dfs(i):
            if i == len(digits):
                return [""]
            
            if i in cache:
                return cache[i]
            
            res = []
            for l in digitMap[digits[i]]:
                for way in dfs(i+1):
                    res.append(l+way)
            cache[i] = res
            return res
        
        return dfs(0)