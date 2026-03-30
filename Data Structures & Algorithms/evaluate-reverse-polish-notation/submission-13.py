import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                subNum = stack.pop()
                stack.append(stack.pop() - subNum)
            elif c == '/':
                divNum = stack.pop()
                stack.append(int(stack.pop()/divNum))
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(c))
        
        return stack[0]