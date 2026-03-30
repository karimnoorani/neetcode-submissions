class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeMap = {}

        for pos, speed in zip(position, speed):
            timeMap[pos] = (target-pos)/speed
        
        position.sort(reverse=True)
        stack = []
        for pos in position:
            if stack and timeMap[stack[-1]] >= timeMap[pos]:
                continue
            stack.append(pos)
        
        return len(stack)
