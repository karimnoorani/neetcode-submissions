class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: deque() for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            for _ in range(len(adj[src])):
                v = adj[src].popleft()
                res.append(v)
                if dfs(v): return True
                adj[src].append(v)
                res.pop()
            return False

        dfs("JFK")
        return res

