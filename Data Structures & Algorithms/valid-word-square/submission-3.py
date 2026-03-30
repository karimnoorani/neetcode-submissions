class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        maxLen = len(max(words, key=len))
        n = max(maxLen, len(words))
        for i in range(n):
            for j in range(n):
                rowChar = words[i][j] if i < len(words) and j < len(words[i]) else ""
                colChar = words[j][i] if j < len(words) and i < len(words[j]) else ""  
                if rowChar != colChar:
                    return False
        
        return True