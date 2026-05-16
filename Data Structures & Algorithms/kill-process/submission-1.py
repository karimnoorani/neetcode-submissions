class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_to_child = defaultdict(list)
        
        for ID, parent_id in zip(pid, ppid):
            parent_to_child[parent_id].append(ID)
        
        res = []
        def dfs(kill):
            res.append(kill)
            for child in parent_to_child[kill]:
                dfs(child)
        dfs(kill)
        return res