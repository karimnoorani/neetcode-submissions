class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {i:0 for i in range(1, n+1)}
        for ai, bi in trust:
            trustMap[bi] += 1
            trustMap[ai] -= 1
        
        for i in range(1, n+1):
            if trustMap[i] == n-1:
                return i
        
        return -1