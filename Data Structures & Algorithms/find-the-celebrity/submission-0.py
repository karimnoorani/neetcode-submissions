# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        score = [0] * n
        
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                if knows(a, b):
                    score[b] += 1
                    score[a] -= 1
        
        for i in range(n):
            if score[i] == n-1:
                return i
        
        return -1