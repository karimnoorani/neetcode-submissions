class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        entering = []
        exiting = []
        
        i = 0
        for a, s in zip(arrival, state):
            heapq.heappush(entering if s == 0 else exiting, [a, i])
            i += 1
        
        last_use = 1
        t = 0
        res = [0 for _ in range(len(state))]
        
        while entering or exiting:
            if last_use == 1:
                if exiting and exiting[0][0] <= t:
                    a, i = heapq.heappop(exiting)
                    res[i] = t
                elif entering and entering[0][0] <= t:
                    a, i = heapq.heappop(entering)
                    res[i] = t
                    last_use = 0
            else:
                if entering and entering[0][0] <= t:
                    a, i = heapq.heappop(entering)
                    res[i] = t
                elif exiting and exiting[0][0] <= t:
                    a, i = heapq.heappop(exiting)
                    res[i] = t
                    last_use = 1
                else:
                    t = min(entering[0][0], exiting[0][0])-1
                    last_use = 1
            
            t += 1
        
        return res
