class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}
        wordDict = set(wordDict)

        def backtracking(i):
            if i == len(s):
                return [""]
            
            if i in cache:
                return cache[i]
            
            res = []
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word not in wordDict:
                    continue
                strings = backtracking(j)
                for subStr in strings:
                    sentence = word
                    if subStr:
                        sentence += " " + subStr
                    res.append(sentence)

            cache[i] = res
            return res
        
        return backtracking(0)
                    