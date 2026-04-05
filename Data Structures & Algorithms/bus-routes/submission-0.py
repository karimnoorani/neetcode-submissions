"""
adjList = {
    
}
"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopToBus = defaultdict(list)
        
        for i, bus in enumerate(routes):
            for stop in bus:
                stopToBus[stop].append(i)

        q = deque([(source, 0)])
        buses_taken = set()
        stops_visited = set([source])

        while q:
            stop, count = q.popleft()

            if stop == target:
                return count
            
            for bus in stopToBus[stop]:
                if bus in buses_taken:
                    continue
                for stop in routes[bus]:
                    if stop in stops_visited:
                        continue
                    q.append([stop, count+1])
                    stops_visited.add(stop)
                buses_taken.add(bus)
        
        return -1