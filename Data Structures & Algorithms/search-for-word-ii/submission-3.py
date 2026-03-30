class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = Trie()
    
    def insertWords(self, words):
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Tree = PrefixTree()
        Tree.insertWords(words)
        ROWS, COLS = len(board), len(board[0])
        visiting = set()
        res = set()
        path = []

        def dfs(Tree, r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] not in Tree.children or (r, c) in visiting:
                return
            
            Tree = Tree.children[board[r][c]]
            visiting.add((r, c))
            path.append(board[r][c])
            
            if Tree.word:
                res.add("".join(path))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(Tree, r+dr, c+dc)
            visiting.remove((r, c))
            path.pop()
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(Tree.root, r, c)

        return list(res)