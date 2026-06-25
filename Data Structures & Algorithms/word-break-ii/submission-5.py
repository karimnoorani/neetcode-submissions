class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}

        def backtrack(index):
            if index == len(s):
                return [""]
            
            if index in cache:
                return cache[index]
            
            result = []
            for end in range(index+1, len(s)+1):
                if s[index:end] not in wordDict:
                    continue
                
                rest = backtrack(end)
                for comb in rest:
                    result.append(s[index:end] + " " + comb if comb != "" else s[index:end])
            
            cache[index] = result
            return cache[index]
        
        return backtrack(0)
