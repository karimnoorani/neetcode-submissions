class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            encoded_string = []
            while stack[-1] != "[":
                encoded_string.append(stack.pop())
            encoded_string = encoded_string[::-1]
            stack.pop() # remove [

            num = 0
            p = 0
            while stack and stack[-1].isdigit():
                num += int(stack.pop())*(10**p)
                p += 1
            stack.append("".join(encoded_string) * num)
        
        return "".join(stack)