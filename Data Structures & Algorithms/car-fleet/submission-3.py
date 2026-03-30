from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeToReachTarget = {}

        for i, pos in enumerate(position):
            timeToReachTarget[pos] = (target-pos)/speed[i]
        
        position.sort()
        print(timeToReachTarget)
        for i in range(len(position)-1, 0, -1):
            if timeToReachTarget[position[i]] >= timeToReachTarget[position[i-1]]:
                timeToReachTarget[position[i-1]] = timeToReachTarget[position[i]]
        
        print(timeToReachTarget)
        
        return len(set(timeToReachTarget.values()))
        