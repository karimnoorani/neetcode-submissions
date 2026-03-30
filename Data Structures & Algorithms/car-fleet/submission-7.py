class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finishMap = {}
        for p, s in zip(position, speed):
            finishMap[p] = (target-p)/s
        
        stack = []
        for p in sorted(position, reverse=True):
            if not stack or finishMap[p] > stack[-1]:
                stack.append(finishMap[p])
        
        return len(stack)