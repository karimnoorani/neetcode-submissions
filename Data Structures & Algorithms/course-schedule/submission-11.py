class Solution:
    def canFinish(self, numCourses: int, preqs: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for a, b in preqs:
            adjList[a].append(b)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True