class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            
            if stack and stack[-1] == abs(asteroid):
                stack.pop()
            elif stack and stack[-1] > abs(asteroid):
                continue
            else:
                stack.append(asteroid)
        
        return stack