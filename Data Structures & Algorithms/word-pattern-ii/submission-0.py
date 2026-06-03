class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        patternMap = {}
        usedMappings = set()
        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True
            
            if i == len(pattern) or j == len(s):
                return False
            
            if pattern[i] in patternMap:
                word = patternMap[pattern[i]]
                if word != s[j:j+len(word)]:
                    return False
                else:
                    return dfs(i+1, j+len(word))
            
            for k in range(j+1, len(s)+1):
                if s[j:k] in usedMappings:
                    continue
                patternMap[pattern[i]] = s[j:k]
                usedMappings.add(s[j:k])
                if dfs(i+1, k):
                    return True
                del patternMap[pattern[i]]
                usedMappings.remove(s[j:k])
            
            return False
        
        return dfs(0, 0)