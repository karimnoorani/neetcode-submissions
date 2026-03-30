class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            if not stack or (target-p)/s > stack[-1]:
                stack.append((target-p)/s)
        
        return len(stack)

