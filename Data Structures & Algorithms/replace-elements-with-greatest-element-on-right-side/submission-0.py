class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        q = deque()

        for i, n in enumerate(arr):
            while q and q[-1][0] <= n:
                q.pop()
            q.append([n, i])
        
        res = [-1 for _ in range(len(arr))]
        for i in range(len(arr)-1):
            while i >= q[0][1]:
                q.popleft()
            res[i] = q[0][0]
        
        return res