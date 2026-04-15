class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        count = 0

        for c in s:
            if stack and stack[-1][0] == c:
                stack.append([c, stack[-1][1]+1])
            else:
                stack.append([c, 1])
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
            
        res = []
        for item in stack:
            res.append(item[0])
        
        return "".join(res)