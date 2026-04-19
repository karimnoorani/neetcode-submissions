class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        entering = deque()
        exiting = deque()
        
        i = 0
        for a, s in zip(arrival, state):
            entering.append([a, i]) if s == 0 else exiting.append([a, i])
            i += 1
        
        last_use = 1
        t = 0
        res = [0 for _ in range(len(state))]
        
        while entering or exiting:
            if last_use == 1:
                if exiting and exiting[0][0] <= t:
                    a, i = exiting.popleft()
                    res[i] = t
                elif entering and entering[0][0] <= t:
                    a, i = entering.popleft()
                    res[i] = t
                    last_use = 0
            else:
                if entering and entering[0][0] <= t:
                    a, i = entering.popleft()
                    res[i] = t
                elif exiting and exiting[0][0] <= t:
                    a, i = exiting.popleft()
                    res[i] = t
                    last_use = 1
                else:
                    t = min(entering[0][0] if entering else float('inf'), exiting[0][0] if exiting else float('inf'))-1
                    last_use = 1
            
            t += 1
        
        return res
