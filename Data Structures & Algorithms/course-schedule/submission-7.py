class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}

        for preqList in prerequisites:
            course, preq = preqList
            courseMap[course].append(preq)
        
        print(courseMap)

        def dfs(course, taken, visited):
            
            if course in visited:
                return
            
            visited.add(course)

            for preq in courseMap[course]:
                dfs(preq, taken, visited)
            
            if set(courseMap[course]).issubset(taken):
                taken.add(course)
            
            visited.remove(course)
        
        taken = set()
        visited = set()
        for course in courseMap:
            if course not in visited and course not in taken:
                dfs(course, taken, visited)
        
        return len(taken) == numCourses