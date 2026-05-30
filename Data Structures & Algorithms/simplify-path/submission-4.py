class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1] == '/':
            path = path[:-1]
        pathList = path[1:].split('/')
        stack = []

        for path in pathList:
            if path == '.' or path == "":
                continue
            elif path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        
        return "/" + "/".join(stack)