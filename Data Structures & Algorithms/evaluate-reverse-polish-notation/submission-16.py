import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                num2 = stack.pop()
                stack.append(stack.pop()-num2)
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                num2 = stack.pop()
                stack.append(int(stack.pop()/num2))
            else:
                stack.append(int(c))
        
        return stack[-1]
