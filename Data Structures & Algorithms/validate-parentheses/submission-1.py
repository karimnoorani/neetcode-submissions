class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingDict = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in matchingDict:
                if stack and stack[-1] == matchingDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False