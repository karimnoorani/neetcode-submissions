class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        maxLen = len(max(words, key=len))
        n = max(maxLen, len(words))
        for i in range(n):
            row = []
            col = []
            for j in range(n):
                if i < len(words) and j < len(words[i]):
                    row.append(words[i][j])
                if j < len(words) and i < len(words[j]):
                    col.append(words[j][i])
            
            if row != col:
                return False
        
        return True