class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            stack.append(char)

            while len(stack) >= k and len(set(stack[-k:])) == 1:
                for _ in range(k):
                    stack.pop()
        
        return "".join(stack)