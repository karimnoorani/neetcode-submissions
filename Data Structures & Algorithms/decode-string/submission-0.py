class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            cur = []
            while stack[-1] != '[':
                cur.append(stack.pop())
            
            stack.pop() # pop [ character
            cur = "".join(cur[::-1]) # reverse to get in correct order

            num = []
            while stack and stack[-1].isdigit():
                num.append(stack.pop())
            
            num = int("".join(num[::-1]))
            for _ in range(num):
                stack.append(cur)
        
        return "".join(stack)
