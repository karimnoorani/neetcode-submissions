import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMap = {i:set() for i in range(9)}
        rowMap = {i:set() for i in range(9)}
        squareMap = {i:set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                
                if board[i][j] == '.':
                    continue
                
                squareNum = (math.floor(i/3)*3)+(math.floor(j/3))

                if board[i][j] in colMap[j] or board[i][j] in rowMap[i] or board[i][j] in squareMap[squareNum]:
                    return False
                
                colMap[j].add(board[i][j])
                rowMap[i].add(board[i][j])
                squareMap[squareNum].add(board[i][j])
        
        return True
                    