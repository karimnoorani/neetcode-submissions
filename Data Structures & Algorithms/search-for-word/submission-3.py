class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] != word[k]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            found = (backtrack(i+1, j, k+1) or backtrack(i, j+1, k+1)
                    or backtrack(i-1, j, k+1) or backtrack(i, j-1, k+1))
            board[i][j] = tmp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0):
                    return True
        
        return False