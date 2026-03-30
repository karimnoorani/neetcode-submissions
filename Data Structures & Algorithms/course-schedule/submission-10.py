class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        visited = set()
        safe = set()
        for a, b in prerequisites:
            adjList[a].append(b)

        def dfs(course):
            if course in visited:
                return False
            if course in safe:
                return True

            visited.add(course)

            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            safe.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
