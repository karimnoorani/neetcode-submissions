class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[b].append(a)
        
        preMap = {}
        def dfs(course):
            if course not in preMap:
                res = set()
                for neigh in adj[course]:
                    res |= dfs(neigh)
                res.add(course)
                preMap[course] = res
            return preMap[course]
        
        for course in range(numCourses):
            dfs(course)
        
        res = []
        for u, v in queries:
            res.append(u in preMap[v])
        
        return res