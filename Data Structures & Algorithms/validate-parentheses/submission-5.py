class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c not in charMap:
                stack.append(c)
            else:
                if not stack or stack.pop() != charMap[c]:
                    return False

        return len(stack) == 0 