class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in charMap:
                if stack and stack[-1] == charMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0