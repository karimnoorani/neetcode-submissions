class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[a].append(b)
        res = []
        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False
            
            if course in visited:
                return True
            
            path.add(course)
            for n in adjList[course]:
                if not dfs(n):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res