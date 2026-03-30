class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            if s[i] == '1':
                continue

            if i == len(s)-1:
                return True
            
            for j in range(max(i+minJump, farthest+1), min(i+maxJump+1, len(s))):
                q.append(j)
            
            farthest = i+maxJump
        
        return False