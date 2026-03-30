import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i:set() for i in range(9)}
        colMap = {i:set() for i in range(9)}
        squareMap = {i:set() for i in range(9)}

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                
                if board[i][j] == '.':
                    continue
                
                square = (math.floor(j/3)*3)+math.floor(i/3)

                if val in rowMap[i] or val in colMap[j] or val in squareMap[square]:
                    return False
                
                rowMap[i].add(val)
                colMap[j].add(val)
                squareMap[square].add(val)

        return True