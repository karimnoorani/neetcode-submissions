class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        cnt = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
                cnt += 1
            elif c == ')':
                if cnt > 0:
                    stack.append(c)
                    cnt -= 1
            else:
                stack.append(c)
        
        filtered = []
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '(' and cnt > 0:
                cnt -= 1
                continue
            filtered.append(stack[i])
        
        return "".join(filtered[::-1])