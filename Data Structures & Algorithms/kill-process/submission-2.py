class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parentToChildren = defaultdict(list)
        result = []

        for ID, parent_id in zip(pid, ppid):
            if parent_id == 0:
                continue
            parentToChildren[parent_id].append(ID)
        

        def killNode(node):
            result.append(node)
            for child in parentToChildren[node]:
                killNode(child)
        
        killNode(kill)
        return result