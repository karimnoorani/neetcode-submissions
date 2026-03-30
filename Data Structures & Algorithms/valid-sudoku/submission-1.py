class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}
        subMap = {}
        for i in range(len(board)):
            rowMap[i] = {}
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                subNum = ((j)//3) + ((i)//3)*3
                # print(i, j, subNum)
                val = board[i][j]
                
                if j not in colMap:
                    colMap[j] = {}
                if subNum not in subMap:
                    subMap[subNum] = {}

                if val in rowMap[i] or val in colMap[j] or val in subMap[subNum]:
                    return False

                rowMap[i][val] = 1
                colMap[j][val] = 1
                subMap[subNum][val] = 1
        
        return True
