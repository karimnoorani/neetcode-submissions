class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        result = []
        current_sentence = []

        def backtrack(index):
            if index == len(s):
                result.append(" ".join(current_sentence))
                return
            
            for end in range(index+1, len(s)+1):
                if s[index:end] in wordDict:
                    current_sentence.append(s[index:end])
                    backtrack(end)
                    current_sentence.pop()
        
        backtrack(0)
        return result
