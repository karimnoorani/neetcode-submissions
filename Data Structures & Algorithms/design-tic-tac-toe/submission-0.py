class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.posDiagMap = defaultdict(int)
        self.negDiagMap = defaultdict(int)
        self.colMap = defaultdict(int)
        self.rowMap = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        self.colMap[col] += 1 if player == 1 else -1
        self.rowMap[row] += 1 if player == 1 else -1
        self.posDiagMap[(row-col)] += 1 if player == 1 else -1
        self.negDiagMap[(row+col)] += 1 if player == 1 else -1

        if self.n in [abs(self.colMap[col]), abs(self.rowMap[row]), abs(self.posDiagMap[(row-col)]), abs(self.negDiagMap[(row+col)])]:
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
