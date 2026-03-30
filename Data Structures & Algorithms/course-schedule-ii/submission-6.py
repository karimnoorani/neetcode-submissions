class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}
        
        for course, preq in prerequisites:
            courseMap[course].append(preq)
        
        visited = set()
        taken = []
        print(courseMap)
        def dfs(n):
            if n in visited:
                return
            
            visited.add(n)

            for preq in courseMap[n]:
                if preq in visited:
                    continue
                
                dfs(preq)
            
            if set(courseMap[n]).issubset(set(taken)):
                taken.append(n)
        
        for i in range(numCourses):
            if i not in visited:
                dfs(i)

        return taken if len(taken) == numCourses else []