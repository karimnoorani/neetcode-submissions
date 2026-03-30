from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        q.append("0000")
        deadends = set(deadends)
        visited = set("0000")

        def shiftIndex(comb, i, shift):
            val = int(comb[i]) + shift
            if val < 0:
                val = 9
            if val > 9:
                val = 0
            return comb[:i] + str(val) + comb[i+1:]

        turns = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                comb = q.popleft()

                if comb == target:
                    return turns
                
                if comb in deadends:
                    continue
                
                for i in range(4):
                    increment = shiftIndex(comb, i, 1)
                    decrement = shiftIndex(comb, i, -1)
                    if increment not in visited:
                        visited.add(increment)
                        q.append(increment)
                    if decrement not in visited:
                        visited.add(decrement)
                        q.append(decrement)
            
            turns += 1
        
        return -1