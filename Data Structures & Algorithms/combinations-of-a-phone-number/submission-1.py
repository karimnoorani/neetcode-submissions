class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {1:[], 2:["A", "B", "C"], 3:["D", "E", "F"], 4:["G","H","I"], 5:["J", "K", "L"], 6:["M", "N", "O"], 7:["P", "Q", "R", "S"], 8:["T", "U", "V"], 9:["W", "X", "Y", "Z"]}
        
        if len(digits) == 0:
            return []

        res = []
        comb = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(comb))
                return
            
            digit = int(digits[i])

            for c in digitMap[digit]:
                comb.append(c.lower())
                dfs(i+1)
                comb.pop()
        
        dfs(0)
        return res