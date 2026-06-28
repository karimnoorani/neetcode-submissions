class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {course: [] for course in range(numCourses)}

        for course, preq in prerequisites:
            adj_list[course].append(preq)
        
        result = []
        visiting = set()
        visited = set()

        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)
            for preq in adj_list[course]:
                if not dfs(preq):
                    return False
            
            result.append(course)
            visiting.remove(course)
            visited.add(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return result