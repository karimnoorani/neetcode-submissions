class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        deadends = set(deadends)
        nextVals = {str(i): [str(i+1), str(i-1)] for i in range(1, 9)}
        nextVals["0"] = ["1", "9"]
        nextVals["9"] = ["0", "8"]
        visited = set(["0000"])
        queue = deque([["0000", 0]])

        while queue:
            lockCode, steps = queue.popleft()

            if lockCode == target:
                return steps
            
            for index in range(len(lockCode)):
                neighbors = nextVals[lockCode[index]]
                for nei in neighbors:
                    nextCode = lockCode[:index] + nei + lockCode[index+1:]
                    if nextCode in deadends or nextCode in visited:
                        continue
                    queue.append([nextCode, steps+1])
                    visited.add(nextCode)
        
        return -1