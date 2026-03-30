class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        
        charMap = {}
        wordMap = {}
        for i, c in enumerate(pattern):
            if c in charMap and charMap[c] != words[i]:
                return False
            if words[i] in wordMap and wordMap[words[i]] != c:
                return False
            charMap[c] = words[i]
            wordMap[words[i]] = c
        
        return True