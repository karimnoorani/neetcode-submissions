class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = defaultdict(int) # person -> people they trust
        trustedByMap = defaultdict(int) # person -> people who trust them
        
        for ai, bi in trust:
            trustMap[ai] += 1
            trustedByMap[bi] += 1
        
        for person in range(1, n+1):
            if trustMap[person] == 0 and trustedByMap[person] == n-1:
                return person
        
        return -1