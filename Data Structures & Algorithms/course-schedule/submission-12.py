class Solution:
    def canFinish(self, numCourses: int, preqs: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for a, b in preqs:
            adjList[a].append(b)
        
        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)
            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True