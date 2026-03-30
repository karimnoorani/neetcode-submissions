class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        closeP = 0
        for c in s:
            closeP += 1 if c == ')' else 0
        
        stack = []
        openP = 0
        for c in s:
            if c == '(':
                if closeP > 0:
                    stack.append(c)
                    openP += 1
                    closeP -= 1
            elif c == ')':
                if openP > 0:
                    stack.append(c)
                    openP -= 1
                else:
                    closeP -= 1
            else:
                stack.append(c)
        
        return "".join(stack)
        