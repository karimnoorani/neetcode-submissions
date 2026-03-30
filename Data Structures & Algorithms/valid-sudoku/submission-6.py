class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {i:set() for i in range(len(board))}
        colMap = {i:set() for i in range(len(board[0]))}
        squareMap = {i:set() for i in range(9)}

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                squareNum = ((r//3)*3)+(c//3)
                if (board[r][c] in rowMap[r] or board[r][c] in colMap[c] 
                    or board[r][c] in squareMap[squareNum]):
                    return False
                
                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                squareMap[squareNum].add(board[r][c])
        
        return True