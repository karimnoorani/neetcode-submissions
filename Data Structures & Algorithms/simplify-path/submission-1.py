class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = []
        for c in path + '/':
            if c == '/':
                cur = "".join(cur)
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = []
            else:
                cur.append(c)
        
        return '/' + '/'.join(stack)
            