class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitToLetter = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7":["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        res = []
        currentChars = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(currentChars))
                return
            
            for char in digitToLetter[digits[i]]:
                currentChars.append(char)
                dfs(i+1)
                currentChars.pop()
        
        dfs(0)
        return res