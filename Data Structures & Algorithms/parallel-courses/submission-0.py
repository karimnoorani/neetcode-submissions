class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        courseToPreq = {i: set() for i in range(1, n+1)}
        preqToCourses = {i: [] for i in range(1, n+1)}
        for preq, course in relations:
            courseToPreq[course].add(preq)
            preqToCourses[preq].append(course)
        
        taken = set()
        q = deque()
        res = 0
        for course in range(1, n+1):
            if len(courseToPreq[course]) == 0:
                q.append(course)
        
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                taken.add(course)

                for nei in preqToCourses[course]:
                    courseToPreq[nei].remove(course)
                    if len(courseToPreq[nei]) == 0:
                        q.append(nei)
            
            res += 1

        return res if len(taken) == n else -1