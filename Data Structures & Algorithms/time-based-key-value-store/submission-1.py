class TimeMap:

    def __init__(self):
        self.timeStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timeStore[key])-1
        res = ""
        
        while l <= r:
            m = (l+r) // 2
            if self.timeStore[key][m][0] <= timestamp:
                res = self.timeStore[key][m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res