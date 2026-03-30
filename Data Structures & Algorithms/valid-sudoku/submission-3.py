import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i:set() for i in range(9)}
        colMap = {i:set() for i in range(9)}
        subMap = {i:set() for i in range(9)}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                square = math.floor(r/3) + (math.floor(c/3)*3)
                
                if val in rowMap[r] or val in colMap[c] or val in subMap[square]:
                    return False
                
                if val != '.':
                    rowMap[r].add(val)
                    colMap[c].add(val)
                    subMap[square].add(val)
                
        return True