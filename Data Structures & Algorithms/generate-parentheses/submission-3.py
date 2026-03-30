class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        perm = []

        def dfs(openCount, closeCount):
            if len(perm) == n*2:
                res.append("".join(perm))
                return
            
            if openCount < n:
                perm.append('(')
                dfs(openCount+1, closeCount)
                perm.pop()
            if closeCount < openCount:
                perm.append(')')
                dfs(openCount, closeCount+1)
                perm.pop()
        
        dfs(0, 0)

        return res