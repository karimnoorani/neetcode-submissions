class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
                continue
            
            if c == '*':
                stars.append(i)
                continue

            if left:
                left.pop()
                continue
            
            if stars:
                stars.pop()
                continue
            
            return False
        
        while left:
            if not stars or left[-1] > stars[-1]:
                return False
            
            left.pop()
            stars.pop()
        
        return len(left) == 0