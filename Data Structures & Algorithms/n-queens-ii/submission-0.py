class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            if r == n:
                return 1
            
            total = 0
            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                total += backtrack(r+1)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            return total
        
        return backtrack(0)