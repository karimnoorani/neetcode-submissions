class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        perm = []
        count = {'(': n, ')': 0}

        def dfs():
            print(perm)
            if len(perm) == n*2:
                res.append("".join(perm))
                return
            
            for c in count:
                if count[c] > 0:
                    perm.append(c)
                    count[c] -= 1
                    if c == '(':
                        count[')'] += 1
                    
                    dfs()

                    perm.pop()
                    count[c] += 1
                    if c == '(':
                        count[')'] -= 1
        
        dfs()
        return res