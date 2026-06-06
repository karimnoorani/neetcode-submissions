class Solution:
    def expand(self, s: str) -> List[str]:
        result = []
        path = []

        def backtracking(index):
            if index == len(s):
                result.append("".join(path))
                return
            
            if s[index] != "{":
                path.append(s[index])
                backtracking(index+1)
                path.pop()
            else:
                right = index
                while s[right] != "}":
                    right += 1
                chars = s[index+1:right].split(',')
                for char in chars:
                    path.append(char)
                    backtracking(right+1)
                    path.pop()
        
        backtracking(0)
        return result
