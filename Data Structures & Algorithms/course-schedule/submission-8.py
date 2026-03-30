class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visitSet = set()
        preqs = {i:[] for i in range(numCourses)}
        
        for crs, preq in prerequisites:
            preqs[crs].append(preq)

        def dfs(crs):
            if crs in visitSet:
                return False

            if preqs[crs] == []:
                return True

            visitSet.add(crs)
            for preq in preqs[crs]:
                if not dfs(preq):
                    return False
            visitSet.remove(crs)
            preqs[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True