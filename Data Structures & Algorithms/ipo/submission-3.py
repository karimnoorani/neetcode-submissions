import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        for p, c in zip(profits, capital):
            heapq.heappush(projects, [c, p])
        
        avail_projects = []
        while k > 0:
            while projects and w >= projects[0][0]:
                c, p = heapq.heappop(projects)
                heapq.heappush(avail_projects, [-p, c])
            
            if len(avail_projects) == 0:
                break
            
            p, c = heapq.heappop(avail_projects)
            w += p*-1
            k -= 1
        
        return w