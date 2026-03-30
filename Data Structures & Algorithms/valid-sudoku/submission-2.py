import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i:[] for i in range(9)}
        colMap = {i:[] for i in range(9)}
        subMap = {i:[] for i in range(9)}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                square = math.floor(r/3) + (math.floor(c/3)*3)
                
                if val in rowMap[r] or val in colMap[c] or val in subMap[square]:
                    return False
                
                if val != '.':
                    rowMap[r].append(val)
                    colMap[c].append(val)
                    subMap[square].append(val)
                
        return True