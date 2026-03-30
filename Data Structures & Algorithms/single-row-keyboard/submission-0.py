class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexMap = {c: i for i, c in enumerate(keyboard)}
        curIndex = 0
        res = 0
        for c in word:
            res += abs(indexMap[c]-curIndex)
            curIndex = indexMap[c]
        
        return res