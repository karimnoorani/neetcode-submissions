class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:
            if not stack or stack[-1] < 0 or n > 0:
                stack.append(n)
                continue
            
            while stack and stack[-1] > 0:
                if abs(n) > abs(stack[-1]):
                    stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(n)
                        break
                elif abs(n) == abs(stack[-1]):
                    stack.pop()
                    break
                else:
                    break

        return stack
