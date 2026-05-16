class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        if kill not in ppid:
            return [kill]
        
        res = [kill]
        for ID, parent_id in zip(pid, ppid):
            if parent_id == kill:
                res += self.killProcess(pid, ppid, ID)
        return res